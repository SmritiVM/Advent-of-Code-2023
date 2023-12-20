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
    total_high = total_low = 0
    state = set_initial_state(MODULE)
    for _ in range(1000):
        high, low = push_button(state, MODULE)
        total_high += high
        total_low += low
    return total_high * total_low

def set_initial_state(MODULE):
    state = {} #{<module>:<state>}
    '''
    For broadcaster -> state is None
    For flipflop -> (0/1, 0/1, 0/1) <off/on> <low/high recent pulse type sent> <low/high pulse inside> 
    For conjunction -> ([input_states], 0/1) <low/high recent pulse type sent>
    '''
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
        state[conjunction] = [inputs_to_conjunction[conjunction], 0]       

    return state

def push_button(state, MODULE):
    # sequence = [] # (<module> <pulse type> <dest>)
    high, low = 0, 1
    queue = deque(['broadcaster'])
    while queue:
        module = queue.popleft()
        type, destinations = MODULE[module]
        #Broadcaster
        if type is None: pulse_type = 0
        
        #Flip flop
        elif type == '%':
            pulse_type = state[module][2] #the pulse type inside the flip flop initially
            state[module][1] = pulse_type #the pulse type the flip flop will send outside

        #Conjunction
        elif type == '&':
            if (all([state[input][1] == 1 for input in state[module][0]])): #if all inputs are high
                pulse_type = 0
            else: pulse_type = 1
            state[module][1] = pulse_type #the pulse type sent out by the conjunction

        for dest in destinations:
            # sequence.append((module, pulse_type, dest))
            if pulse_type == 0: low += 1
            else: high += 1
            if dest not in MODULE: continue
            dest_type = MODULE[dest][0]
            if dest_type == '%':
                if not flip_the_flop(dest, pulse_type, state): continue
            queue.append(dest)

    return high, low

def flip_the_flop(dest, pulse_type, state):
    #If pulse is high, ignore
    if pulse_type == 1: return False
    #Pulse is low
    #If status is off, switch on and set pulse inside to high
    if state[dest][0] == 0: state[dest][0], state[dest][2] = 1, 1
    #If status is on, switch off and set pulse inside to low
    elif state[dest][0] == 1: state[dest][0], state[dest][2] = 0, 0
    return True


path = "20.Pulse_Propagation\input.txt"
MODULE = get_puzzle(path)
print(get_total_pulses(MODULE))