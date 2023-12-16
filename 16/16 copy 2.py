def get_puzzle(path):
    with open(path) as file:
        return [list(line.strip()) for line in file]

def get_max_energized(CONTRAPTION):
    rows, columns = len(CONTRAPTION), len(CONTRAPTION[0])
    max_energized = 0
    #Check 1st row
    for j in range(columns):
        if j == 0:
            max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '>')))
        elif j == columns - 1:
            max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '<')))
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, 'v')))

    #Check last row
    for j in range(columns):
        if j == 0:
            max_energized = max(max_energized, get_total_energized(CONTRAPTION, (rows - 1, j, '>')))
        elif j == columns - 1:
            max_energized = max(max_energized, get_total_energized(CONTRAPTION, (rows - 1, j, '<')))
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (0, j, '^')))

    #Check 1st column
    for i in range(1, rows - 1): #corners checked in rows
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (i, 0, '>')))

    #Check last column
    for i in range(1, rows - 1): #corners checked in rows
        max_energized = max(max_energized, get_total_energized(CONTRAPTION, (i, columns - 1, '<')))
    
    return max_energized

    

def get_total_energized(CONTRAPTION, start):
    visited = dfs(CONTRAPTION, start)
    # print(sorted(visited))
    return len(visited)

def dfs(CONTRAPTION, start):
    
    visited = set()
    visited_points = set()
    stack = [start] #<i, j, direction>
    while stack:
        # if len(stack) == 5: break
        # print(stack) # visited)
        node = stack.pop()
        visited.add(node)
        visited_points.add((node[0], node[1]))
        next = get_next(node, CONTRAPTION)
        check_next(next, node[2], CONTRAPTION, stack, visited, visited_points)
    return visited_points
        

def get_next(node, CONTRAPTION):
    i, j, direction = node
    if CONTRAPTION[i][j] in '/\\': return i,j
    if CONTRAPTION[i][j] == '|' and direction not in '^v': return i,j
    if CONTRAPTION[i][j] == '-' and direction not in '><': return i,j
    if direction == '>':
        return i, j + 1
    elif direction == '<':
        return i, j - 1
    elif direction == '^':
        return i - 1, j
    elif direction == 'v':
        return i + 1, j

def is_valid(i, j, rows, columns):
    return not any([i < 0, i >= rows, j < 0, j >= columns])

def check_next(next, direction, CONTRAPTION, stack, visited, visited_points):
    #Check what next is and reflect
    rows, columns = len(CONTRAPTION), len(CONTRAPTION[0])
    i, j = next
    if not is_valid(i, j, rows, columns): return
    visited.add((i, j, direction))
    visited_points.add((i, j))
    # Empty space
    if CONTRAPTION[i][j] == '.':
        stack.append((i, j, direction))

    # Mirror
    elif CONTRAPTION[i][j] == '/':
        if direction == '>': #right -> up
            if is_valid(i - 1, j, rows, columns) and not check_visited(visited,  (i - 1,j,'^')): 
                stack.append((i - 1, j, '^'))
                visited.add((i - 1, j, '^'))
        elif direction == '<': #left -> down
            if is_valid(i + 1, j, rows, columns) and not check_visited(visited,  (i + 1, j, 'v')): 
                stack.append((i + 1, j, 'v'))
                visited.add((i + 1, j, 'v'))
        elif direction == '^': #up -> right
            if is_valid(i, j + 1, rows, columns) and not check_visited(visited,  (i, j + 1, '>')): 
                stack.append((i, j + 1, '>'))
                visited.add((i, j + 1, '>'))
        elif direction == 'v': #down -> left
            if is_valid(i, j - 1, rows, columns) and not check_visited(visited,  (i, j - 1, '<')): 
                stack.append((i, j - 1, '<'))
                visited.add((i, j - 1, '<'))
    elif CONTRAPTION[i][j] == "\\":
        if direction == '>': #right -> down
            if is_valid(i + 1, j, rows, columns) and not check_visited(visited,  (i + 1, j, 'v')): 
                stack.append((i + 1, j, 'v'))
                visited.add((i + 1, j, 'v'))
        elif direction == '<': #left -> up
            if is_valid(i - 1, j, rows, columns) and not check_visited(visited,  (i - 1, j, '^')): 
                stack.append((i - 1, j, '^'))
                visited.add((i - 1, j, '^'))
        elif direction == '^': #up -> left
            if is_valid(i, j - 1, rows, columns) and not check_visited(visited,  (i, j - 1, '<')): 
                stack.append((i, j - 1, '<'))
                visited.add((i, j - 1, '<'))
        elif direction == 'v': #down -> right
            if is_valid(i, j + 1, rows, columns) and not check_visited(visited,  (i, j + 1, '>')): 
                stack.append((i, j + 1, '>'))
                visited.add((i, j + 1, '>'))
    # Splitter
    elif CONTRAPTION[i][j] == '|':
        if direction in '><':
            if is_valid(i - 1, j, rows, columns) and not check_visited(visited,  (i - 1, j, '^')): 
                stack.append((i - 1, j, '^'))
                visited.add((i - 1, j, '^'))
            if is_valid(i + 1, j, rows, columns) and not check_visited(visited,  (i + 1, j, 'v')): 
                stack.append((i + 1, j, 'v'))
                visited.add((i + 1, j, 'v'))
        elif direction == '^':
            if is_valid(i - 1, j, rows, columns) and not check_visited(visited,  (i - 1, j, '^')): 
                stack.append((i - 1, j, '^'))
                visited.add((i - 1, j, '^'))
        else:
            if is_valid(i + 1, j, rows, columns) and not check_visited(visited,  (i + 1, j, 'v')): 
                stack.append((i + 1, j, 'v'))
                visited.add((i + 1, j, 'v'))
    elif CONTRAPTION[i][j] == '-':
        if direction in '^v':
            if is_valid(i, j - 1, rows, columns) and not check_visited(visited,  (i, j - 1, '<')): 
                stack.append((i, j - 1, '<'))
                visited.add((i, j - 1, '<'))
            if is_valid(i, j + 1, rows, columns) and not check_visited(visited,  (i, j + 1, '>')): 
                stack.append((i, j + 1, '>'))
                visited.add((i, j + 1, '>'))
        elif direction == '<':
            if is_valid(i, j - 1, rows, columns) and not check_visited(visited,  (i, j - 1, '<')): 
                stack.append((i, j - 1, '<'))
                visited.add((i, j - 1, '<'))
        else:
            if is_valid(i, j + 1, rows, columns) and not check_visited(visited, (i, j + 1, '>')): 
                stack.append((i, j + 1, '>'))
                visited.add((i, j + 1, '>'))

def check_visited(visited, next):
    return (next in visited)

path = "16\input.txt"
CONTRAPTION = get_puzzle(path)
print(get_max_energized(CONTRAPTION))