from collections import defaultdict

def get_puzzle(path):
    with open(path) as file:
        return file.read().split(',')

def sum_of_hash_values(SEQUENCE):
    total = 0
    for sequence in SEQUENCE:
        total += get_hash_value(sequence)
    return total

def get_hash_value(sequence):
    current_value = 0
    for char in sequence:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value

def total_focusing_power(SEQUENCE):
    # Get hashmap {<Box no>:[[<label> <focal length>], ...]}
    BOXES = generate_boxmap(SEQUENCE)
    
    # Generate hashmap {<label>:(<box no>, <slot no>, <focal length>)}
    LENS = generate_lensmap(BOXES)

    #Find focusing power
    total_power = 0
    for lens in LENS:
        box_no, slot, focal_length = LENS[lens]
        total_power += (box_no + 1) * slot * focal_length
    return total_power

def generate_boxmap(SEQUENCE):
    boxes = defaultdict(dict)
    for sequence in SEQUENCE:
        # Check the operator
        if '=' in sequence:
            label, focal_length = sequence.split('=')
            hash_value = get_hash_value(label)
            boxes[hash_value][label] = int(focal_length)
        elif '-' in sequence:
            label = sequence[:-1]
            hash_value = get_hash_value(label)
            boxes[hash_value].pop(label, None)
    return boxes
            
def generate_lensmap(BOXES):
    lens = {}
    for box_no in BOXES:
        for slot, label in enumerate(BOXES[box_no], start=1):
            lens[label] = (box_no, slot, BOXES[box_no][label])
    return lens

    

path = "15.Lens_Library\input.txt"
SEQUENCE = get_puzzle(path)

#Part 1
print(sum_of_hash_values(SEQUENCE))

#Part 2
print(total_focusing_power(SEQUENCE))

'''
rn=1
cv = 0
r -> 114 => cv = 114, cv *=17 = 1938 %256 = 146
n -> 110 => cv = 146 + 110 ...cv = 0
= -> 61...cv = 13
1 -> 49...cv = 30
'''