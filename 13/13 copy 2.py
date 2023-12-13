COUNT = 0
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Get all patterns
    PATTERNS = []
    for line in file.read().split('\n\n'):
        PATTERNS.append(line.split('\n'))
    return PATTERNS

def summarize_notes(PATTERNS):
    #LOR => line of reflection
    #Find total no. of vertical and horizontal LORs
    vertical = horizontal = 0
    sum = 0
    for pattern in PATTERNS:
        horizontal = find_horizontal_mirror(pattern, smudges=1)
        vertical = find_vertical_mirror(pattern, smudges=1)
        sum += vertical + 100 * horizontal
    return sum

def find_horizontal_mirror(pattern, smudges=0):
    for i, line in enumerate(pattern):
        if i + 1 == len(pattern): return 0
        pairs_to_check = [(c1, c2) for line1, line2 in zip(pattern[i::-1], pattern[i+1:])
                          for c1, c2 in zip(line1, line2)]
        if sum(1 for c1,c2 in pairs_to_check if c1 == c2) == len(pairs_to_check) - smudges:
            return i + 1
        
def find_vertical_mirror(pattern, smudges=0):
    transpose = list(zip(*pattern))
    return find_horizontal_mirror(transpose, smudges)
    

path = "13\input.txt"
PATTERNS = get_puzzle(path)
# print(len(PATTERNS))
print(summarize_notes(PATTERNS))       