import re
def get_puzzle(path, discrete = True):
    with open(path) as file:
        sheet = file.read().split('\n')
        return parse_input(sheet, discrete)

def parse_input(sheet, discrete = True):
    time_array = re.findall("\d+", sheet[0])
    distance_array = re.findall("\d+", sheet[1])
    if discrete:
        TIME = list(map(int, time_array))
        DISTANCE = list(map(int, distance_array))
    else:
        TIME = [int(''.join(time_array))]
        DISTANCE = [int(''.join(distance_array))]
    return TIME, DISTANCE

def total_winning_ways(TIME, DISTANCE):
    total_ways = 1
    for time, distance in zip(TIME, DISTANCE):
        total_ways *= count_winning_ways(time, distance)
    return total_ways

def count_winning_ways(time, distance):
    number_of_winning_ways = 0
    for ms in range(1, time + 1):
        distance_travelled = find_distance(ms, time)
        if distance_travelled > distance: number_of_winning_ways += 1
    return number_of_winning_ways

def find_distance(ms, time):
    #Holding the button for 'ms' amount of time
    #Thus remaining time will be time - ms
    remain = time - ms
    #Speed of boat is equal to ms
    speed = ms
    #Distance travelled is speed * remaining time
    distance_travelled = speed * remain
    return distance_travelled


path = "6.Wait_For_It\input.txt"

#Part 1
TIME, DISTANCE = get_puzzle(path)
print(total_winning_ways(TIME, DISTANCE))

#Part 2
TIME, DISTANCE = get_puzzle(path, discrete = False)
print(total_winning_ways(TIME, DISTANCE))