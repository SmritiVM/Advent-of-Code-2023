import re
from math import lcm

def get_puzzle(path):
    with open(path) as file:
        document = file.read().split('\n')
        return parse_input(document)
    
def parse_input(document):
    INSTRUCTIONS = document[0]
    NODES = {}
    START, END = [], []
    for line in document[2:]:
        node, left, right = re.findall("[1-9A-Z]+", line)
        NODES[node] = (left, right)
        if node[-1] == 'A': START.append(node)
        elif node[-1] == 'Z': END.append(node)
    return INSTRUCTIONS, NODES, START, END


def total_steps(INSTRUCTIONS, NODES, START=[], END=[], dest_fixed=True):
    #Part1
    if dest_fixed:
        return find_steps('AAA', INSTRUCTIONS, NODES, dest_fixed)

    #Part2
    #Finding number of steps for each node to reach a Z end and then finding LCM
    steps_per_node = []
    for node in START:
        steps = find_steps(node, INSTRUCTIONS, NODES, END, dest_fixed)
        steps_per_node.append(steps)
    return lcm(*steps_per_node)

def find_steps(node, INSTRUCTIONS, NODES, END=[], dest_fixed=True):
    instruction_number = 0
    steps = 0
    total_instructions = len(INSTRUCTIONS)
    current_node = node
    while (dest_fixed and current_node != 'ZZZ') or (not dest_fixed and current_node not in END):
        current_instruction = INSTRUCTIONS[instruction_number]
        if current_instruction == "L":
            current_node = NODES[current_node][0]
        else:
            current_node = NODES[current_node][1]
        instruction_number = (instruction_number + 1) % total_instructions
        steps += 1
    return steps


path = "08.Haunted_Wasteland\input.txt"
INSTRUCTIONS, NODES, START, END = get_puzzle(path)

#Part1
print(total_steps(INSTRUCTIONS, NODES))

#Part2
print(total_steps(INSTRUCTIONS, NODES, START, END, dest_fixed=False))