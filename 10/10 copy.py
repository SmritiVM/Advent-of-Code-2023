from collections import deque, defaultdict

def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    MAZE = [line.strip() for line in file]
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
                  'J': [[-1,0], [0,-1]], '7': [[1,0], [0,-1]], 'F': [[1,0], [0,1]],
                  'S': [[-1,-1], [-1,0], [-1,1], [0,-1], [0, 1],[1,-1], [1,0], [1,1]], '.': []}
    
    adjacent = defaultdict(set)
    rows, cols = len(MAZE), len(MAZE[0])
    print(rows, cols)
    for x in range(rows):
        for y in range(cols):
            point = MAZE[x][y]
            if point == 'S': continue
            for dx, dy in neighbours[point]:
                x_, y_ = x + dx, y + dy
                if all([x >= 0, x < rows, y >= 0 and y < cols]):
                    adjacent[(x, y)].add((x_, y_))

    print(adjacent)

    #Finding the adjacency list for start
    adjacent_start = set()
    for u in adjacent:
        for v in adjacent[u]:
            if v == start:
                adjacent_start.add(u)
    adjacent[start] = adjacent_start

            

    distance = defaultdict(lambda: float('INF'))
    queue = deque([(start, 0)])
    while queue:
        node, current_distance = queue.popleft()
        distance[node] = current_distance
        for vertex in adjacent[node]:
            if distance[vertex] > current_distance:
                queue.append((vertex, current_distance + 1))
    
    print(max(distance.values()))


    
path = "10\input.txt"
MAZE, start = get_puzzle(path)
print(get_farthest_point(MAZE, start))


# N, S, E, W = -1, +1, +1j, -1j
# exits = {'|': (N, S), '-': (E, W),
#          'L': (N, E), 'J': (N, W),
#          '7': (S, W), 'F': (S, E),
#          '.': (), 'S': (N, E, S, W)}

# board = {(p:=2*i+2j*j): [p+e for e in exits[c]]
#     for i,r in enumerate(open(path))
#     for j,c in enumerate(r.strip())}
# start = next(k for k,v in board.items() if len(v)==4)
# graph = defaultdict(set)
# for p, qs in board.items():
#     for q in qs:
#         graph[p].add(q)
#         graph[q].add(p)
# dist = defaultdict(lambda: 1_000_000)
# q = deque([(start,0)])
# while q:
#     n, d = q.popleft()
#     dist[n] = d
#     for e in graph[n]:
#         if dist[e] > d: q.append((e, d+1))

# print(max(dist.values())//2)

'''
.....
.F-7.
.|.|.
.L-J.
.....

'''