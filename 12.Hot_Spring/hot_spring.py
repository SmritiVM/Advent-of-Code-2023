from functools import lru_cache

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    RECORDS = {}
    for index, line in enumerate(file):
        record, condition = line.strip('\n').split(" ")
        RECORDS[index] = (record, tuple(map(int, condition.split(','))))
    return RECORDS

def sum_of_arrangements(RECORDS, unfold=False):
    total_arrangements = 0
    for line in RECORDS:
        record, conditions = RECORDS[line]
        if unfold:
            record = '?'.join([record] * 5)
            conditions = conditions * 5
        total_arrangements += get_arrangements(record, conditions)
    return total_arrangements

@lru_cache
def get_arrangements(record, conditions):
    #Empty record
    if not record:
        if not conditions: return 1
        return 0
    
    #Startswith .
    if record[0] == '.':
        return get_arrangements(record[1:], conditions)
    
    #Startswith ? => 2 choices, replace by . or replace by #
    if record[0] == '?':
        choice1 = get_arrangements('#' + record[1:], conditions)
        choice2 = get_arrangements('.' + record[1:], conditions)
        return choice1 + choice2
    
    #Startswith # => check if matches conditions[0]
    if not conditions: return 0
    if len(record) < conditions[0]: return 0
    if any(x == '.' for x in record[0:conditions[0]]): return 0
    if len(conditions) > 1:
        if len(record) < conditions[0] + 1 or record[conditions[0]] == "#": #if there aren't enough records for the next group or if the next char is # => cannot be the starting of a new group
            return 0
        return get_arrangements(record[conditions[0] + 1:], conditions[1:]) #+1 because we cannot consider immediate next
    else:
        # return get_arrangements(record[conditions[0]:], conditions[1:])
        return 0 if any([char == '#' for char in record[conditions[0]:]]) else 1
    

    

path = "12.Hot_Spring\input.txt"
RECORDS = get_puzzle(path)

#Part 1
print(sum_of_arrangements(RECORDS))

#Part 2
print(sum_of_arrangements(RECORDS, unfold = True))