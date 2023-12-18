from collections import defaultdict
DIRECTIONS = {'R':(0, 1), 'L':(0, -1), 'U':(-1, 0), 'D':(1, 0)}

def get_puzzle(path):
    with open(path) as file:
        return [line.strip().split() for line in file]

def find_lava_area(PLAN):
    boundary = [(0, 0)]
    prev = (0, 0)
    rows_end = columns_end = 0
    rows_start = columns_start = 1e100
    row_limits = defaultdict(lambda: (1e100, 0))
    col_limits = defaultdict(lambda: (1e100, 0))
    for instruction in PLAN:
        direction, distance = instruction[0], int(instruction[1])
        while distance > 0:
            offset_x, offset_y = DIRECTIONS[direction]
            next = (prev[0] + offset_x, prev[1] + offset_y)
            rows_end = max(rows_end, next[0])
            columns_end = max(columns_end, next[1])
            rows_start = min(rows_start, next[0])
            columns_start = min(columns_start, next[1])
            row_limits[next[0]] = (min(row_limits[next[0]][0], next[1]), max(row_limits[next[0]][1], next[1]))
            # col_limits[next[1]] = (min(col_limits[next[1]][0], next[0]), max(row_limits[next[0]][1], next[1]))
            boundary.append(next)
            prev = next
            distance -= 1
    
    # print(row_limits)
    # for i in range(row)
    # print(rows, columns)
    # interior_points = 0
    # print(rows_start, rows_end)
    # print(columns_start, columns_end)
    # for i in range(rows_start, rows_end + 1):
    #     for j in range(columns_start, columns_end + 1):
    #         if (i, j) in boundary: continue
    #         min_col, max_col = row_limits[i]
    #         if min_col < j < max_col:
    #             interior_points += 1
    # print(interior_points)

    # print(boundary)
    # print(row_limits)
    # Find area 
    area = 0
    for i in range(len(boundary) - 1):
        a = boundary[i]
        b = boundary[i + 1]
        #Finding determinant and adding to area
        # https://en.wikipedia.org/wiki/Shoelace_formula
        area +=  (a[0]*b[1] - a[1]*b[0])
    # print(area)
    perimeter = len(boundary)
    interior_points = abs(area) // 2 - perimeter//2 + 1
    # https://en.wikipedia.org/wiki/Pick's_theorem
    # return (interior_points + len(boundary)//2 - 1)
    return (interior_points + perimeter)
 
path = "18\input.txt"
PLAN = get_puzzle(path)
print(find_lava_area(PLAN))