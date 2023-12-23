from collections import defaultdict
def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def generate_adjacency(TRAIL, consider_slopes=True):
    known_directions = {'.':['>','<','^','v'], '#':[]}
    adjacent = defaultdict(set)
    for x in range(rows):
        for y in range(cols):
            cell = TRAIL[x][y]
            if cell in known_directions: 
                possible_directions = known_directions[cell]
            elif consider_slopes: possible_directions = [cell]
            else: possible_directions = ['>','<','^','v']
            
            for direction in possible_directions:
                dx, dy = DIRECTIONS[direction]
                x_, y_ = x + dx, y + dy
                if is_valid(x_, y_, TRAIL): 
                    adjacent[(x,y)].add((x_, y_, 1))
                    adjacent[(x_,y_)].add((x, y, 1))
    return adjacent

def modify_adjacency(adjacent):
    while True:
        for cell, neighbours in adjacent.items():
            #Continuous stretches that only have 2 adjacent nodes are compressed
            if len(neighbours) == 2:
                neighbour1, neighbour2 = neighbours
                x1, y1, length1 = neighbour1
                x2, y2, length2 = neighbour2

                #Since current cell can be eliminated, remove current cell
                del adjacent[cell] 
                #Then remove cell from adjacent of neighbours
                adjacent[(x1, y1)].remove(cell + (length1,))
                adjacent[(x2, y2)].remove(cell + (length2,))
                
                #Merging the endpoints and making them adjacent
                adjacent[(x1, y1)].add((x2, y2, length1 + length2))
                adjacent[(x2, y2)].add((x1, y1, length1 + length2))
                break #since size of dictionary changes and we need to start over
        else:
            break
    return adjacent

def get_longest_path(ADJACENT):
    stack = [(0, 1, 0)]
    visited = set()
    max_length = 0
    while stack:
        x, y, length = stack.pop()
        if length == -1:
            visited.remove((x, y))
            continue
        if x == rows - 1 and y == cols - 2:
            max_length = max(max_length, length)
            continue
        if (x, y) in visited: 
            continue
        visited.add((x, y))
        stack.append((x, y, -1))
        for x_, y_, length_ in ADJACENT[(x, y)]:
            stack.append((x_, y_, length + length_))
    return max_length

def is_valid(x, y, TRAIL):
    return (0 <= x < rows) and (0 <= y < cols) and (TRAIL[x][y] != "#")


path = "23.A_Long_Walk\input.txt"
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
TRAIL = get_puzzle(path)
rows, cols = len(TRAIL), len(TRAIL[0])

# #Part 1
# ADJACENT = generate_adjacency(TRAIL, consider_slopes=True)
# print(get_longest_path(ADJACENT))

# Part 2
ADJACENT = generate_adjacency(TRAIL, consider_slopes=False)
ADJACENT = modify_adjacency(ADJACENT)
print(get_longest_path(ADJACENT))
