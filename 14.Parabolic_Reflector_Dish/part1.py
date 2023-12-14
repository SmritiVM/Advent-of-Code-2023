def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Store as a matrix
    return [list(line.strip('\n')) for line in file]

def get_total_load(ROCKS):
    # go line by line and send up until prev is rock
    tilt_rocks(ROCKS)
    # print(*ROCKS, sep = '\n')
    total_load = 0
    for load, line in enumerate(ROCKS[::-1], start=1):
        round_rocks = line.count('O')
        total_load += round_rocks * load
    return total_load

def tilt_rocks(ROCKS):
    for y in range(len(ROCKS)):
        for x in range(len(ROCKS[0])):
            if ROCKS[y][x] == 'O':
                send_up(ROCKS, y, x)

def send_up(ROCKS, y, x):
    if y == 0: return
    start = y - 1
    while start >= -1:
        current = ROCKS[start][x]
        if current in 'O#' or start == -1:
            #set next rock
            ROCKS[y][x] = '.'
            ROCKS[start + 1][x] = 'O'
            return
        start -= 1
            


path = "14.Parabolic_Reflector_Dish\input.txt"
ROCKS = get_puzzle(path)
print(get_total_load(ROCKS))