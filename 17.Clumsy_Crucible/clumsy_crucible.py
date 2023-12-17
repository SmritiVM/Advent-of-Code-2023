from heapq import heappop, heappush

def get_puzzle(path):
    with open(path) as file:
       return [list(map(int, line.strip())) for line in file]
    
def find_minimum_heat_loss(MAP, min_moves, max_moves):
    end = (rows - 1, columns - 1)
    heap = [] #[heat loss so far, (x, y, direction, moves)]
    heat_losses = {} # {<city>:heat_loss} city = (x, y, direction, moves)

    #For start, the possible directions are already known so adding them
    for direction in '>v':
        heappush(heap, (0, (0, 0, direction, 0)))
    
    while heap:
        heat_loss, city = heappop(heap)
        
        if city in heat_losses: continue
        heat_losses[city] = heat_loss

        x, y, direction, moves = city
        if (x, y) == end and moves >= min_moves:
            return heat_loss

        neighbours = find_neighbours(city, min_moves, max_moves)

        for neighbour in neighbours:
            if neighbour not in heat_losses or new_heat_loss < heat_losses[city]:
                new_heat_loss = heat_loss + MAP[neighbour[0]][neighbour[1]]
                heappush(heap, (new_heat_loss, neighbour))

def find_neighbours(city, min_moves, max_moves):
    x, y, direction, moves = city
    neighbours = []
    for next_direction in DIRECTIONS:
        dx, dy = DIRECTIONS[next_direction]
        x_, y_ = x + dx, y + dy
        if not in_bounds((x_, y_)): continue
        if next_direction == get_reverse(direction): continue
        if next_direction == direction:
            current_moves = moves + 1
        else:
            current_moves = 1

        if current_moves > max_moves: continue
        if direction != next_direction and moves < min_moves: continue

        neighbours.append((x_, y_, next_direction, current_moves))
    return neighbours

def in_bounds(city):
    i, j = city
    return all([i >= 0, i < rows, j >= 0, j < columns])


def get_reverse(direction):
    reverse = {'>':'<', '<':'>', '^':'v', 'v':'^'}
    return reverse[direction]

path = "17.Clumsy_Crucible\input.txt"
MAP = get_puzzle(path)
rows, columns = len(MAP), len(MAP[0])
DIRECTIONS = {'>':(0, 1), '<':(0, -1), '^':(-1, 0), 'v':(1, 0)}

#Part 1
print(find_minimum_heat_loss(MAP, min_moves = 1, max_moves = 3))

#Part 2
print(find_minimum_heat_loss(MAP, min_moves = 4, max_moves = 10))