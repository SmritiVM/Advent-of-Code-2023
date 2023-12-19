from collections import defaultdict
from itertools import combinations_with_replacement  
import re
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    workflows, parts = file.read().split('\n\n')
    WORKFLOW = defaultdict(dict) #{<workflow>:{<cond>:<redirect>, None:<default>}}
    PART = defaultdict(lambda: {'x': 0, 'm': 0, 'a':0, 's':0})

    #WORKFLOW
    for line in workflows.split():
        pos = line.find('{')
        label = line[:pos]
        values = line[pos + 1: -1].split(',')
        for value in values:
            if ':' in value: 
                condition, redirect = value.split(':')
                WORKFLOW[label][(condition[0], condition[1], int(condition[2:]))] = redirect
            else: WORKFLOW[label][None] = value
            
    

    #PART
    for index, line in enumerate(parts.split()):
        values = re.findall('[0-9]+', line)
        PART[index]['x'] = int(values[0])
        PART[index]['m'] = int(values[1])
        PART[index]['a'] = int(values[2])
        PART[index]['s'] = int(values[3])
    
    return WORKFLOW, PART

def sum_of_accepted_parts(part, state):
    if state == "A":
        return (part["x"].stop - part["x"].start) * (part["m"].stop - part["m"].start) * (part["a"].stop - part["a"].start) * (part["s"].stop - part["s"].start)
    elif state == "R":
        return 0
    part = part.copy()
    workflow = WORKFLOW[state]
    total = 0
    last = ''
    for condition, redirect in workflow.items():
        if condition == None: 
            last = redirect
            continue
        curr, op, value = condition
        if op == '>':
            dest_range = range(value + 1, part[curr].stop)
            after_range = range(part[curr].start, value + 1)
        else:
            dest_range = range(part[curr].start, value)
            after_range = range(value, part[curr].stop)
        part[curr] = dest_range
        total += sum_of_accepted_parts(part, redirect)
        part[curr] = after_range
    total += sum_of_accepted_parts(part, last)
    return total

            

        

path = "19\input.txt"
WORKFLOW, PART = get_puzzle(path)
# print(WORKFLOW)
start = {"x": range(1, 4001), "m": range(1, 4001), "a": range(1, 4001), "s": range(1, 4001)}
print(sum_of_accepted_parts(start, "in"))
