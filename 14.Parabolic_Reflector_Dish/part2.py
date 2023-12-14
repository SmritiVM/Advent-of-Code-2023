from copy import deepcopy
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Store as a matrix
    return [list(line.strip('\n')) for line in file]

def get_total_load(ROCKS):
    start, limit, cycle_outputs = find_cycle(ROCKS)
    ROCKS = cycle_outputs[start + (1000000000 - start) % limit - 1]

    total_load = 0
    for load, line in enumerate(ROCKS[::-1], start=1):
        round_rocks = line.count('O')
        total_load += round_rocks * load
    return total_load

def find_cycle(ROCKS):
    cycle_outputs = []
    current_cycle = 0
    while True:
        new_config = tilt_rocks(ROCKS)
        if new_config in cycle_outputs:
            index = cycle_outputs.index(new_config)
            start, limit = index, current_cycle - index
            return start, limit, cycle_outputs 
        cycle_outputs.append(new_config)
        current_cycle += 1

def tilt_rocks(ROCKS):
    for y in range(len(ROCKS)):
        for x in range(len(ROCKS[0])):
            if ROCKS[y][x] == 'O':
                send_north(ROCKS, y, x)
    # print('N', *ROCKS, sep = '\n')
    for y in range(len(ROCKS)):
        for x in range(len(ROCKS[0])):
            if ROCKS[y][x] == 'O':
                send_west(ROCKS, y, x)
    # print('W',*ROCKS, sep = '\n')
    for y in range(len(ROCKS) - 1, -1, -1):
        for x in range(len(ROCKS[0]) - 1, -1, -1):
            if ROCKS[y][x] == 'O':
                send_south(ROCKS, y, x)
    # print('S',*ROCKS, sep = '\n')
    for y in range(len(ROCKS)):
        for x in range(len(ROCKS[0]) - 1, -1, -1):
            if ROCKS[y][x] == 'O':
                send_east(ROCKS, y, x)
    # print('E',*ROCKS, sep = '\n')
    return deepcopy(ROCKS)


def send_north(ROCKS, y, x):
    if y == 0: return
    start = y - 1
    while start >= -1:
        if start == -1 or ROCKS[start][x] in 'O#':
            #set next rock
            ROCKS[y][x] = '.'
            ROCKS[start + 1][x] = 'O'
            return
        start -= 1

def send_west(ROCKS, y, x):
    if x == 0: return
    start = x - 1
    while start >= -1:
        if start == -1 or ROCKS[y][start] in 'O#':
            #set next rock
            ROCKS[y][x] = '.'
            ROCKS[y][start + 1] = 'O'
            return
        start -= 1

def send_south(ROCKS, y, x):
    end = len(ROCKS)
    if y == end - 1: return
    start = y + 1
    while start <= end:
        if start == end or ROCKS[start][x] in 'O#':
            #set next rock
            ROCKS[y][x] = '.'
            ROCKS[start - 1][x] = 'O'
            return
        start += 1

def send_east(ROCKS, y, x):
    end = len(ROCKS[0])
    if x == end - 1: return
    start = x + 1
    while start <= end:
        if start == end or ROCKS[y][start] in 'O#':
            #set next rock
            ROCKS[y][x] = '.'
            ROCKS[y][start - 1] = 'O'
            return
        start += 1


path = "14.Parabolic_Reflector_Dish\input.txt"
ROCKS = get_puzzle(path)
print(get_total_load(ROCKS))