from collections import deque, defaultdict

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    MAZE = file.read().split('\n')
    for x in range(len(MAZE)):
        for y in range(len(MAZE[0])):
            if MAZE[x][y] == 'S':
                return MAZE, (x,y)

def get_farthest_point(MAZE, start):
    loop = get_biggest_loop(MAZE, start)

def get_biggest_loop(MAZE, start):
    #Pipes and their permissible neighbours
    '''
    | -> up & down, - => left & right
    L => top & right, J => top & left
    7 => bottom & left, F => bottom & right
    '''
    neighbours = {'|': [[-1,0], [1,0]], '-': [[0,-1], [0,1]], 'L': [[-1,0], [0,1]],
                  'J': [[-1,0], [0,-1]], '7': [[1,0], [0,-1]], 'F': [[1,0], [0,1]]}
    symbols =list(neighbours.keys()) + ['S']
    #Important cond: connect to exactly 2 pipes
    # Or use a queue to check
    #Return as {(<x1>, <y1>):<distance from start>, (<x2>, <y2>),...}
    #maintain distance array too
    #Check all 6 combinations for start and then run BFS for each combination to find the loop
    x,y = start
    biggest_loop = {}
    for combination in neighbours.values():
        temp_loop = []
        for dx, dy in combination:
            try:
                x_, y_ = x + dx, y + dy
                if x_ < 0 or y_ < 0: break
                if MAZE[x + dx][y + dy] in symbols:
                    temp_loop.append((x_, y_))
            except: break
        if len(temp_loop) == 2:
            queue = deque(temp_loop)
            print("outside bfs", queue)
            loop = bfs(MAZE, queue, neighbours, symbols)
            if len(loop)> len(biggest_loop): biggest_loop = loop
                       

    print(list(biggest_loop.keys()))

def bfs(MAZE, queue, neighbours, symbols):
    #BFS
    loop = defaultdict(lambda: 0) #visited points in the loop
    while queue:
        print("running queue")
        x,y = queue.popleft()
        temp_loop = defaultdict(lambda: 0)
        connected = 0
        symbol = MAZE[x][y]
        if symbol == '.': continue
        if symbol == 'S': continue
        #Check all permissible sides for the node
        #i.e if connected to 2 symbols
        for dx, dy in neighbours[symbol]:
            try:
                x_, y_ = x + dx, y + dy
                if x_ < 0 or y_ < 0: break
                if MAZE[x + dx][y + dy] in symbols:
                    connected += 1
                    if ((x_, y_) not in temp_loop):
                        temp_loop[(x_, y_)] = 0
            except: break
        if connected == 2:
            print(x,y, temp_loop)
            loop.update(temp_loop)
            queue.extend(list(temp_loop.keys()))
            print("insidie bfs", queue)
    
    return loop

    
path = "10\sampleinput.txt"
MAZE, start = get_puzzle(path)
print(get_farthest_point(MAZE, start))

'''
.....
.F-7.
.|.|.
.L-J.
.....

'''