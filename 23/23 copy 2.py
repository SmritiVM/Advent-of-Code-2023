from collections import defaultdict
def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def generate_adjacency(TRAIL):
    adjacent = defaultdict(set)
    rows, cols = len(TRAIL), len(TRAIL[0])
    for x in range(rows):
        for y in range(cols):
            cell = TRAIL[x][y]
            # if cell == '#': possible_directions = []
            if cell in ".>v": 
                possible_directions = ['>','<','^','v']
            else: possible_directions = []
            for direction in possible_directions:
                dx, dy = DIRECTIONS[direction]
                x_, y_ = x + dx, y + dy
                if is_valid(x_, y_, rows, cols, TRAIL): 
                    adjacent[(x,y)].add((x_, y_, 1))
                    adjacent[(x_,y_)].add((x, y, 1))

    # rows, cols = len(TRAIL), len(TRAIL[0])
    while True:
        for node, edges in adjacent.items():
            if len(edges) == 2:
                a, b = edges
                adjacent[a[:2]].remove(node + (a[2],))
                adjacent[b[:2]].remove(node + (b[2],))
                adjacent[a[:2]].add((b[0], b[1], a[2] + b[2]))
                adjacent[b[:2]].add((a[0], a[1], a[2] + b[2]))
                del adjacent[node]
                break
        else:
            break
    return adjacent

def get_longest_path(TRAIL, ADJACENT):
    rows, cols = len(TRAIL), len(TRAIL[0])
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

def is_valid(x, y, rows, cols, TRAIL):
    return (0 <= x < rows) and (0 <= y < cols) and (TRAIL[x][y] in ".>v")


path = "23\sampleinput.txt"
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
TRAIL = get_puzzle(path)
ADJACENT = generate_adjacency(TRAIL)
print(ADJACENT)

#Part 1
print(get_longest_path(TRAIL, ADJACENT))

#Part 2
# ADJACENT = modify_adjacency(ADJACENT)
print(get_longest_path(TRAIL, ADJACENT))
