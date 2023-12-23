def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def get_longest_path(TRAIL):
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
        if (x, y) in visited: continue
        visited.add((x, y))
        stack.append((x, y, -1))

        cell = TRAIL[x][y]
        if cell == '.':
            possible_directions = ['>','<','^','v']
        elif cell == '#':
            possible_directions = []
        else: possible_directions = [cell]
        for direction in possible_directions:
            dx, dy = DIRECTIONS[direction]
            x_, y_ = x + dx, y + dy
            if is_valid(x_, y_, rows, cols, TRAIL):
                stack.append((x_, y_, length + 1))
    return max_length

def is_valid(x, y, rows, cols, TRAIL):
    return (0 <= x < rows) and (0 <= y < cols) and (TRAIL[x][y] != '#')


path = "23\input.txt"
TRAIL = get_puzzle(path)
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
print(get_longest_path(TRAIL))

