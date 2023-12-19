from collections import defaultdict
from functools import reduce

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    workflows = file.read().split('\n\n')[0]
    WORKFLOW = defaultdict(dict) #{<workflow>:{<cond>:<redirect>, None:<default>}}, <cond> = (part_type, operation, threshold)
    for line in workflows.split():
        pos = line.find('{')
        label = line[:pos]
        values = line[pos + 1: -1].split(',')
        for value in values:
            if ':' in value: 
                condition, redirect = value.split(':')
                part_type, operation, threshold = condition[0], condition[1], int(condition[2:])
                WORKFLOW[label][(part_type, operation, threshold)] = redirect
            else: WORKFLOW[label][None] = value
    return WORKFLOW

def sum_of_accepted_parts(WORKFLOW, PART):
    return predict_acceptable(PART, "in", WORKFLOW)

def predict_acceptable(parts, state, WORKFLOW):
    if state == "A":
        return reduce((lambda x, y: x * y), [stop - start for start, stop in parts.values()]) 
    elif state == "R":
        return 0
    parts = parts.copy() # to prevent modification of original dictionary due to mutability
    workflow = WORKFLOW[state]
    total = 0
    for condition, redirect in workflow.items():
        if condition == None: 
            total += predict_acceptable(parts, redirect, WORKFLOW)
            break
        part_type, operation, threshold = condition
        start, stop = parts[part_type]
        if operation == '<':
            new_start, new_stop = start, threshold
            remain_start, remain_stop = threshold, stop
        elif operation == '>':
            new_start, new_stop = threshold + 1, stop
            remain_start, remain_stop = start, threshold + 1
        parts[part_type] = (new_start, new_stop)
        total += predict_acceptable(parts, redirect, WORKFLOW)
        parts[part_type] = (remain_start, remain_stop)

    return total

path = "19.Aplenty\input.txt"
WORKFLOW = get_puzzle(path)
PART = {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)} #{<part type>:(<start>, <stop>)}
print(sum_of_accepted_parts(WORKFLOW, PART))
