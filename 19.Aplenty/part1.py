from collections import defaultdict
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
            if ':' in value: condition, redirect = value.split(':')
            else: condition, redirect = None, value
            WORKFLOW[label][condition] = redirect
    

    #PART
    for part_no, line in enumerate(parts.split()):
        values = re.findall('[0-9]+', line)
        PART[part_no]['x'] = int(values[0])
        PART[part_no]['m'] = int(values[1])
        PART[part_no]['a'] = int(values[2])
        PART[part_no]['s'] = int(values[3])
    
    return WORKFLOW, PART

def sum_of_accepted_parts(WORKFLOW, PART):
    accepted = find_accepted_parts(WORKFLOW, PART)
    total = 0
    for part_no in accepted:
        total += sum(PART[part_no].values())
    return total

def find_accepted_parts(WORKFLOW, PART):
    accepted = []
    for part_no in PART:
        x,m,a,s = PART[part_no].values()
        state = 'in'
        while state not in 'AR':
            workflow = WORKFLOW[state]
            for condition, redirect in workflow.items():
                if condition == None: 
                    state = redirect
                elif eval(condition) is True:
                    state = redirect
                    break
        if state == 'A': accepted.append(part_no)
    return accepted
            

path = "19.Aplenty\input.txt"
WORKFLOW, PATH = get_puzzle(path)
print(sum_of_accepted_parts(WORKFLOW, PATH))