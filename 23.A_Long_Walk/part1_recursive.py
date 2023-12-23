import sys
# print(sys.getrecursionlimit())
sys.setrecursionlimit(3000)

def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def get_longest_path(TRAIL):
    paths = []
    current_path = ""
    rows = len(TRAIL)
    cols = len(TRAIL[0])
    find_path(0, 1, TRAIL, rows, cols, paths, current_path)
    max_path_length = 0
    for path in paths:
        max_path_length = max(max_path_length, len(path))
    return max_path_length

def find_path(x, y, TRAIL, rows, cols, paths, current_path):
    #Base case i.e reaching bottom-most cell
    if x == rows - 1 and y == cols - 2:
        paths.append(current_path)
        return
    
    #Marking current cell as blocked
    cell = TRAIL[x][y]
    TRAIL[x][y] = "#"
    if cell == '.':
        possible_directions = ['>','<','^','v']
    elif cell == '#':
        possible_directions = []
    else: possible_directions = [cell]
    for direction in possible_directions:
        dx, dy = DIRECTIONS[direction]
        x_, y_ = x + dx, y + dy
        if is_valid(x_, y_, rows, cols, TRAIL):
            current_path += direction
            find_path(x_, y_, TRAIL, rows, cols, paths, current_path)
            #Backtrack by removing last direction
            current_path = current_path[:-1]
    #Mark the current cell as unblocked
    TRAIL[x][y] = cell

def is_valid(x, y, rows, cols, TRAIL):
    return (0 <= x < rows) and (0 <= y < cols) and (TRAIL[x][y] != '#')


path = "23\input.txt"
TRAIL = get_puzzle(path)
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
# DIRECTIONS = {'.':[(0,1), (0,-1), (1,0), (-1,0)],
#               '>':[(0,1)], '<':[(0,-1)], '^':[(-1,0)], 'v':[(1,0)]} #<type of cell>:<valid directions>
print(get_longest_path(TRAIL))
