def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)

def parse_input(input):
    HISTORY = []
    for line in input:
        HISTORY.append(list(map(int, line.split())))
    return HISTORY

def get_extrapolated_sum(HISTORY):
    total_forward = total_backward = 0
    for history in HISTORY:
        extrapolated_values = get_extrapolated_value(history)
        total_forward += extrapolated_values[0]
        total_backward += extrapolated_values[1]
    return total_forward, total_backward #return as (<part1 answer>, <part2 answer>)

def get_extrapolated_value(history):
    current_sequence = history
    sequences = [history]
    while not all([num == 0 for num in current_sequence]):
        difference_sequence = []
        for i in range(1, len(current_sequence)):
            diff = current_sequence[i] - current_sequence[i - 1]
            difference_sequence.append(diff)
        sequences.append(difference_sequence)
        current_sequence = difference_sequence
    
    #Reverse iteration
    extrapolated_forward = extrapolated_backward = 0
    while sequences:
        current_sequence = sequences.pop()
        first_value, last_value = current_sequence[0], current_sequence[-1]
        extrapolated_forward, extrapolated_backward = last_value + extrapolated_forward, first_value - extrapolated_backward
    return extrapolated_forward, extrapolated_backward

path = "09.Mirage_Maintenance\input.txt"
HISTORY = get_puzzle(path)
print(get_extrapolated_sum(HISTORY))

