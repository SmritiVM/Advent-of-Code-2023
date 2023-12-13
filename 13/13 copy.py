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
    for pattern in PATTERNS:
        direction, lines = find_lor(pattern)
        if direction == "V": vertical += lines
        else: horizontal += lines
    return vertical + 100 * horizontal

def find_lor(pattern):
    # print(pattern)
    #Check vertical
    rows, columns = len(pattern), len(pattern[0])

    #Check horizontal
    lor_pos = check_lor_exists(pattern, rows)
    if lor_pos: return 'H', lor_pos

    #Transpose pattern
    transpose = []
    for j in range(columns):
        line = ''
        for i in range(rows):
            line += pattern[i][j]
        transpose.append(line)
    return "V", check_lor_exists(transpose, columns)

def check_lor_exists(pattern, length):
    lor_pos = 0 #lor b/w lor_pos and lor_pos + 1 i.e storing the lower limit
    while lor_pos < length - 1:
        lines_above = lor_pos + 1
        lines_below = length - lor_pos - 1
        if lines_above < lines_below:
            above, below = pattern[lor_pos::-1], pattern[lor_pos + 1: lor_pos + 1 + lines_above]
        else:
            above, below = pattern[lor_pos:lor_pos - lines_below:-1], pattern[lor_pos + 1:]
        if above == below:
            return lor_pos + 1
        lor_pos += 1
    return 0


path = "13\input.txt"
PATTERNS = get_puzzle(path)
print(summarize_notes(PATTERNS))



        