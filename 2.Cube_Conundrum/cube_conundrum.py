TOTAL = {'red':12, 'green':13, 'blue':14}
current_max = {'red': 0, 'green':0, 'blue':0}

def find_sums(input):
    valid_ID_sum = power_sum = 0
    for line in input:
        game_ID, power = process_input(line)
        valid_ID_sum += game_ID
        power_sum += power
    return(valid_ID_sum, power_sum)

def process_input(line):
    # Split and check the input
    game, sets = line.split(":")
    total_draws = valid_draws = 0
    current_max['red'] = current_max['green'] = current_max['blue'] = 0
    for set in sets.strip().split(';'):
        draws = set.strip().split(',')
        for draw in draws:
            total_draws += 1
            count, colour = draw.strip().split(' ')
            set_current_max(count, colour)
            if is_valid(count, colour):
                valid_draws += 1


    if total_draws == valid_draws:
        game_ID = int(game[5:])
    else:
        game_ID = 0
    power = current_max['red'] * current_max['green'] * current_max['blue']
    return game_ID, power

def is_valid(count, colour):
    return int(count) <= TOTAL[colour]

def set_current_max(count, colour):
    current_max[colour] = max(current_max[colour], int(count))


with open("2. Cube Conundrum\input.txt") as input:
    print(*find_sums(input))