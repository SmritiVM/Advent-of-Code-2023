def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def get_max_energized(CONTRAPTION):
    rows, columns = len(CONTRAPTION), len(CONTRAPTION[0])
    max_energized = 0
    #Check 1st row
    for j in range(columns):
        if j == 0: max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '>')))
        elif j == columns - 1: max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '<')))
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, 'v')))

    #Check last row
    for j in range(columns):
        if j == 0: max_energized = max(max_energized, get_total_energized(CONTRAPTION, (rows - 1, j, '>')))
        elif j == columns - 1: max_energized = max(max_energized, get_total_energized(CONTRAPTION, (rows - 1, j, '<')))
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '^')))

    #Check 1st column
    for i in range(1, rows - 1): #corners already checked in rows
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (i, 0, '>')))

    #Check last column
    for i in range(1, rows - 1): #corners already checked in rows
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (i, columns - 1, '<')))
    
    return max_energized

def get_total_energized(CONTRAPTION, start):
    energized = dfs(CONTRAPTION, start) #set of all energized points
    return len(energized)

def dfs(CONTRAPTION, start):
    visited = set() #{(i, j, direction)} storing points with direction visited
    energized = set() # {(i, j)} storing just the coordinates
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        energized.add((node[0], node[1]))
        next = get_next(node, CONTRAPTION)
        check_next(next, node[2], CONTRAPTION, stack, visited, energized)
    return energized
        

def get_next(node, CONTRAPTION):
    i, j, direction = node
    if CONTRAPTION[i][j] in '/\\|-': return i,j
    DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
    row_offset, col_offset = DIRECTIONS[direction]
    return i + row_offset, j + col_offset

def is_valid_coordinate(point: tuple, rows: int, columns: int):
    i, j = point
    return not any([i < 0, i >= rows, j < 0, j >= columns])

def check_next(next: tuple, direction: str, CONTRAPTION: list, stack: list, visited: set, energized: set):
    rows, columns = len(CONTRAPTION), len(CONTRAPTION[0])
    i, j = next
    if not is_valid_coordinate(next, rows, columns): return # if next is out of bounds, we don't check
    energized.add((i, j)) # else next has been energized

    # Check what next is and reflect
    # Empty space
    if CONTRAPTION[i][j] == '.':
        stack.append((i, j, direction))
        return

    DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}
    # Storing NEXT = {<symbol>:{<direction>:(<reflected direction>,..), ...}, ...}
    NEXT = { '/':{'>':('^'), '<':('v'), '^':('>'), 'v':('<')},
            '\\':{'>':('v'), '<':('^'), '^':('<'), 'v':('>')},
             '|':{'>':('^','v'), '<':('^','v'), '^':('^'), 'v':('v')},
             '-':{'>':('>'), '<':('<'), '^':('>','<'), 'v':('>','<')}
           }

    reflected_directions = NEXT[CONTRAPTION[i][j]][direction]
    for reflected_direction in reflected_directions:
        row_offset, col_offset = DIRECTIONS[reflected_direction]
        next = (i + row_offset, j + col_offset, reflected_direction)
        if is_valid_coordinate(next[:-1], rows, columns) and not is_visited(visited, next): 
            stack.append(next)
            visited.add(next)

def is_visited(visited, next):
    return next in visited

path = "16.Floor_Lava\input.txt"
CONTRAPTION = get_puzzle(path)

#Part 1
print(get_total_energized(CONTRAPTION, start=(0,0,'>')))

#Part 2
print(get_max_energized(CONTRAPTION))