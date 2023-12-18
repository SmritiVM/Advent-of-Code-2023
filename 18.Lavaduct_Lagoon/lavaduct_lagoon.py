from collections import defaultdict

DIRECTIONS = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0)}
CODE = {0:'R', 1:'D', 2:'L', 3:'U'}

def get_puzzle(path, modify=False):
    with open(path) as file:
        return parse_input(file, modify)
    
def parse_input(file, modify=False):
    if not modify:
        return [line.strip().split() for line in file]
    PLAN = []
    for line in file:
        instruction = line.strip().split()[2][1:-1] #index 2 => color code, [1:-1] => to strip ( and )
        distance, direction = int(instruction[1:-1], 16), CODE[int(instruction[-1])]
        PLAN.append([direction, distance])
    return PLAN

def find_lava_area(PLAN):
    boundary = find_boundary(PLAN)

    # Shoelace formula
    area = 0
    for a,b in zip(boundary[:-1], boundary[1:]):
        area +=  (a[0]*b[1] - a[1]*b[0])

    # Pick's theorem
    perimeter = len(boundary)
    interior_points = abs(area) // 2 - perimeter//2 + 1
    return interior_points + perimeter
 
path = "18.Lavaduct_Lagoon\sampleinput.txt"

def find_boundary(PLAN):
    boundary = [(0, 0)]
    prev = (0, 0)
    for instruction in PLAN:
        direction, distance = instruction[0], int(instruction[1])
        while distance > 0:
            x, y = prev
            dx, dy= DIRECTIONS[direction]
            next = (x + dx, y + dy)
            boundary.append(next)
            prev = next
            distance -= 1
    return boundary[:-1] #starting position also gets added to boundary so exculding that

#Part 1
PLAN = get_puzzle(path)
print(find_lava_area(PLAN))

#Part 2
PLAN = get_puzzle(path, modify=True)
print(find_lava_area(PLAN))