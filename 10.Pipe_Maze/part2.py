from collections import deque, defaultdict

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    MAZE = [list(line.strip()) for line in file]

    #Pipes and their permissible neighbours
    '''
    | -> up & down, - => left & right
    L => top & right, J => top & left
    7 => bottom & left, F => bottom & right
    '''
    neighbours = {'|': [[-1,0], [1,0]], '-': [[0,-1], [0,1]], 'L': [[-1,0], [0,1]],
                  'J': [[-1,0], [0,-1]], '7': [[1,0], [0,-1]], 'F': [[1,0], [0,1]], '.': []}
    
    adjacent = defaultdict(set)
    rows, cols = len(MAZE), len(MAZE[0])
    for x in range(rows):
        for y in range(cols):
            point = MAZE[x][y]
            if point == 'S': 
                start = (x,y)
                continue
            for dx, dy in neighbours[point]:
                x_, y_ = x + dx, y + dy
                if all([x >= 0, x < rows, y >= 0 and y < cols]):
                    adjacent[(x, y)].add((x_, y_))

    #Finding the adjacency list for start
    adjacent_start = set()
    for u in adjacent:
        for v in adjacent[u]:
            if v == start:
                adjacent_start.add(u)
    adjacent[start] = adjacent_start
    return MAZE, adjacent, start

def get_biggest_loop(MAZE, adjacent, start):
    stack = deque([(start, None)])
    previous = {}
    while stack:
        node, prev = stack.pop()
        for vertex in adjacent[node]:
            if vertex == prev: continue
            previous[vertex] = node
            stack.append((vertex, node))
        if node == start and prev is not None: break

    #Getting path of traversal
    path = [start]
    while True:
        vertex = previous[path[-1]]
        if vertex == start: break
        path.append(vertex)
    print(path)
    return path

def get_farthest_distance(path):
    return len(path)//2
    
def find_enclosed_tiles(path):
    #Shoelace formula and picks theorem
    area = 0
    for a,b in zip(path, path[1:]+ [path[0]]):
        #Finding determinant and adding to area
        # https://en.wikipedia.org/wiki/Shoelace_formula
        area +=  (a[0]*b[1] - a[1]*b[0])
    # https://en.wikipedia.org/wiki/Pick's_theorem
    return abs(area//2 + len(path)//2 - 1)

path = "10.Pipe_Maze\input.txt"
MAZE, ADJACENT, START = get_puzzle(path)
path = get_biggest_loop(MAZE, ADJACENT, START)

#Part 1
print(get_farthest_distance(path))

#Part 2
print(find_enclosed_tiles(path))