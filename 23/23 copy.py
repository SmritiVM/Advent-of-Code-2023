from collections import deque
def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def get_longest_path(TRAIL):
    paths = []
    current_path = ""
    rows = len(TRAIL)
    cols = len(TRAIL[0])
    # path = get_biggest_loop(TRAIL, (0, 1))
    return len(find_path(TRAIL, rows, cols, current_path))
    # find_path(0, 1, TRAIL, rows, cols, paths, current_path)
    # max_path_length = 0
    # for path in paths:
    #     max_path_length = max(max_path_length, len(path))
    # return max_path_length

def find_path(TRAIL, rows, cols, current_path):
    stack = [(0, 1, 'v')]
    visited = {(0,1)}
    while stack:
        x, y, current_path = stack.pop()
        if x == rows - 1 and y == cols - 2:
            return current_path
        cell = TRAIL[x][y]
        if cell == '.':
            possible_directions = ['>','<','^','v']
        elif cell == '#':
            possible_directions = []
        else: possible_directions = [cell]
        for direction in possible_directions:
            dx, dy = DIRECTIONS[direction]
            x_, y_ = x + dx, y + dy
            if is_valid(x_, y_, rows, cols, TRAIL) and (x_, y_) not in visited:
                current_path += direction
                stack.append((x_, y_, current_path))
                visited.add((x_, y_))
  
def is_valid(x, y, rows, cols, TRAIL):
    return (0 <= x < rows) and (0 <= y < cols) and (TRAIL[x][y] != '#')


path = "23\input.txt"
TRAIL = get_puzzle(path)
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
# print(get_longest_path(TRAIL))
