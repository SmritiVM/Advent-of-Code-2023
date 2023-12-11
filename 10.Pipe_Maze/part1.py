from collections import deque, defaultdict

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    MAZE = [line.strip() for line in file]

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

    return adjacent, start

def get_farthest_distance(adjacent, start):
    distance = defaultdict(lambda: float('INF'))
    queue = deque([(start, 0)])
    while queue:
        node, current_distance = queue.popleft()
        distance[node] = current_distance
        for vertex in adjacent[node]:
            if distance[vertex] > current_distance:
                queue.append((vertex, current_distance + 1))
    
    return max(distance.values())
    
path = "10.Pipe_Maze\input.txt"
ADJACENT, START = get_puzzle(path)
print(get_farthest_distance(ADJACENT, START))