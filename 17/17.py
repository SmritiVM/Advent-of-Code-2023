from heapq import heappop, heappush

def get_puzzle(path):
    with open(path) as file:
       return [list(map(int, line.strip())) for line in file]
    
def find_minimum_heat_loss(MAP):
    heap = [(0, 0, 0, None, 0)] #heat loss so far, x, y, direction, moves
    visited = set() #(x, y, direction)
    cumulative_heat_loss = {}
    while heap:
        city = heappop(heap)
        heat_loss, x, y, direction, moves = city
        if (x, y) == (rows - 1, columns - 1): #dest reached
            return heat_loss
        if (x, y, ) in visited: continue
        visited.add((x, y, invalid_dir))
        neighbours = find_neighbours(city)
        # print(neighbours)
        for neighbour in neighbours:
            x_, y_, direction, invalid_dir, moves = neighbour
            current_heat_loss = heat_loss + MAP[x_][y_]
            if cumulative_heat_loss.get((x_, y_), 1e100) <= current_heat_loss: 
                # print('hey', cumulative_heat_loss)
                continue
            cumulative_heat_loss[(x_, y_)] = current_heat_loss
            heappush(heap, (current_heat_loss, x_, y_, direction, invalid_dir, moves))
        # print(heap)
        print(cumulative_heat_loss)
    # print(cumulative_heat_loss[(rows - 1, columns - 1)])



def find_neighbours(city):
    # print(city)
    heat_loss, x, y, prev_dir, invalid_dir, moves = city
    neighbours = []
    for direction in DIRECTIONS:
        dx, dy = DIRECTIONS[direction]
        x_, y_ = x + dx, y + dy
        if not in_bounds((x_, y_)): continue
        if is_behind((x_, y_), (x, y)): continue
        # if direction == invalid_dir: continue
        current_moves = 1
        if direction == prev_dir:
            if moves == 3: continue
            current_moves += moves
        neighbours.append((x_, y_, direction, get_disallowed_direction(direction), current_moves))
    return neighbours

def in_bounds(city):
    i, j = city
    return not any([i < 0, i >= rows, j < 0, j >= columns])

def is_behind(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return x1 < x2 or y1 < y2

def get_disallowed_direction(direction):
    if direction == '>': return '<'
    elif direction == '<': return '>'
    if direction == '^': return 'v'
    if direction == 'v': return '^'

path = "17\sampleinput.txt"
MAP = get_puzzle(path)
rows, columns = len(MAP), len(MAP[0])
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
print(find_minimum_heat_loss(MAP))