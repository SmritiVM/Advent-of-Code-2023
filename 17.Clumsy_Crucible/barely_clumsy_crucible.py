from heapq import heappop, heappush

def get_puzzle(path):
    with open(path) as file:
       return [list(map(int, line.strip())) for line in file]
    
def find_minimum_heat_loss(MAP):
    heap = [(0, 0, 0, '>', '<', 0), (0, 0, 0, 'v', '<', 0)] #heat loss so far, x, y, prev_dir, invalid_dir, moves
    visited = set() #(x, y, direction, moves)
    cumulative_heat_loss = {}
    while heap:
        city = heappop(heap)
        heat_loss, x, y, prev_dir, invalid_dir, moves = city
        if (x, y) == (rows - 1, columns - 1): #dest reached
            return heat_loss
        if (x, y, prev_dir, moves) in visited: continue
        visited.add((x, y, prev_dir, moves))
        neighbours = find_neighbours(city)
        for neighbour in neighbours:
            x_, y_, direction, invalid_dir, moves = neighbour
            current_heat_loss = heat_loss + MAP[x_][y_]
            if cumulative_heat_loss.get((x_, y_, direction, moves), 1e100) <= current_heat_loss: 
                continue
            cumulative_heat_loss[(x_, y_, direction, moves)] = current_heat_loss
            heappush(heap, (current_heat_loss, x_, y_, direction, invalid_dir, moves))


def find_neighbours(city):
    x, y, prev_dir, invalid_dir, moves = city[1:]
    neighbours = []
    for direction in DIRECTIONS:
        dx, dy = DIRECTIONS[direction]
        x_, y_ = x + dx, y + dy
        if not in_bounds((x_, y_)): continue
        if direction == invalid_dir: continue
        current_moves = 1
        if direction == prev_dir:
            if moves == 3: continue
            current_moves += moves
        neighbours.append((x_, y_, direction, get_disallowed_direction(direction), current_moves))
    return neighbours

def in_bounds(city):
    i, j = city
    return not any([i < 0, i >= rows, j < 0, j >= columns])

def get_disallowed_direction(direction):
    if direction == '>': return '<'
    elif direction == '<': return '>'
    if direction == '^': return 'v'
    if direction == 'v': return '^'

path = "17.Clumsy_Crucible\input.txt"
MAP = get_puzzle(path)
rows, columns = len(MAP), len(MAP[0])
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
print(find_minimum_heat_loss(MAP))