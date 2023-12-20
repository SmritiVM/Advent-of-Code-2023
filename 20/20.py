from collections import deque, defaultdict
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    MODULE = {} #{<name of mod>: (<type>, [<dest modules>])}
    for line in file:
        name, destinations = line.strip().split(' -> ')
        if name == "broadcaster": type = None
        else: type, name = name[0], name[1:]
        MODULE[name] = (type, destinations.split(', '))
    return MODULE

def get_total_pulses(MODULE):
    cycle_pattern = find_cycle(MODULE) #{<cycle>:(<high>, <low>)}

def find_cycle(MODULE):
    cycle_pattern = {}
    iteration = 1
    current_cycle = []
    #Set initial states
    state = set_initial_state(MODULE)
    # print(state)
    current_cycle = push_button(state, MODULE)
    print(current_cycle)
    current_cycle = push_button(state, MODULE)
    print(current_cycle)
    current_cycle = push_button(state, MODULE)
    print(current_cycle)
    current_cycle = push_button(state, MODULE)
    print(current_cycle)
    current_cycle = push_button(state, MODULE)
    print(current_cycle)
    # while tuple(current_cycle) not in cycle_pattern:
    #     break

def set_initial_state(MODULE):
    state = {} #{<module>:<state>}
    #For broadcaster -> state is None
    #For flipflop -> (0/1, 0/1, 0/1) <off/on> <low/high pulse inside> <low/high recent pulse type sent>
    #For conjunction -> ([input_states], 0/1)
    inputs_to_conjunction = defaultdict(list) #{<module>:[<inputs>]}
    for module in MODULE:
        type, destinations = MODULE[module]
        if type is None: state[module] = None
        elif type == '%': state[module] = [0, 0, 0] #initially off
        elif type == '&': state[module] = {}
        for dest in destinations:
            if dest in MODULE and MODULE[dest][0] == '&': #if it routes to a conjunction module
                inputs_to_conjunction[dest].append(module)

    for conjunction in inputs_to_conjunction:
        state[conjunction] = [inputs_to_conjunction[conjunction], None]
            

    return state


def push_button(state, MODULE):
    sequence = [] # <module> <pulse type> <dest>
    queue = deque(['broadcaster'])
    while queue:
        module = queue.popleft()
        # print(module)
        type, destinations = MODULE[module]
        #Broadcaster
        if type is None:
            for dest in destinations:
                #All destinations are only flip flops
                #Pulse is low
                #If status is off, switch on and send high
                if state[dest][0] == 0: state[dest][0:2] = [1, 1]
                #If status is on, switch off and send low
                elif state[dest][0] == 1: state[dest][0:2] = [0, 0]
                sequence.append((module, 0, dest))
                queue.append(dest)
        
        #Flip flop
        elif type == '%':
            pulse_type = state[module][1]
            for dest in destinations:
                sequence.append((module, pulse_type, dest))
                if dest not in MODULE: continue
                dest_type = MODULE[dest][0]
                if dest_type == '%':
                    #If pulse is high, ignore
                    if pulse_type == 1: continue
                    #Pulse is low
                    #If status is off, switch on and send high
                    if state[dest][0] == 0: state[dest][0:2] = [1, 1]
                    #If status is on, switch off and send low
                    elif state[dest][0] == 1: state[dest][0:2] = [0, 0]
                else:
                    state[dest][1] = pulse_type
                queue.append(dest)
            state[module][2] = pulse_type
        
        #Conjunction
        elif type == '&':
            if (all([state[input][2] == 1 for input in state[module][0]])):
                pulse_type = 0
            else: pulse_type = 1
            # print(module, pulse_type, 'l')
            for dest in destinations:
                sequence.append((module, pulse_type, dest))
                if dest not in MODULE: continue
                dest_type = MODULE[dest][0]
                if dest_type == '%':
                    #If pulse is high, ignore
                    if pulse_type == 1: continue
                    #Pulse is low
                    #If status is off, switch on and send high
                    if state[dest][0] == 0: state[dest][0:2] = [1, 1]
                    #If status is on, switch off and send low
                    elif state[dest][0] == 1: state[dest][0:2] = [0, 0]
                    # print(state)
                else:
                    state[dest][1] = pulse_type
                queue.append(dest)
            state[module][1] = pulse_type
    # print(state)   
    return sequence


path = "20\sampleinput1.txt"
MODULE = get_puzzle(path)
# print(MODULE)
print(get_total_pulses(MODULE))