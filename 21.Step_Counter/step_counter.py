def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    PLOT = [list(line.strip()) for line in file]
    for x in range(len(PLOT)):
        for y in range(len(PLOT[0])):
            if PLOT[x][y] == 'S':
                return PLOT, (x,y)

def get_garden_plots_covered(PLOT, START, steps):
    queue = [START]
    for _ in range(steps):
        queue = cover_adjacent(PLOT, queue)
    return len(queue)

def cover_adjacent(PLOT, queue):
    next = set()
    while queue:
        x, y = queue.pop()
        neighbours = [(0,1), (1,0), (0,-1), (-1,0)]
        for dx, dy in neighbours:
            x_, y_ = x + dx, y + dy
            inbound_x, inbound_y = get_inbound_coord(x_, y_)
            if PLOT[inbound_x][inbound_y] != '#':
                next.add((x_, y_))
    return list(next)

def get_inbound_coord(x, y):
    return x % rows, y % cols
    
# goal = 26501365
# def f(n):
#     a0 = 3682
#     a1 = 32768
#     a2 = 90820

#     b0 = a0
#     b1 = a1-a0
#     b2 = a2-a1
#     return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
# print(f(goal//131))

def get_garden_plots_covered_infinite(PLOT, START, steps):
    '''
    Let garden plots covered = y
    Quadratic equation of the form y = ax2 + bx + c
    First three values in this sequence are for x = 0 -> y0, x = 1 -> y1, x = 2 -> y2
    '''
    #Finding value for y0, y1, y2
    length = len(PLOT)
    offset = steps % length
    y0 = get_garden_plots_covered(PLOT, START, steps=offset)
    y1 = get_garden_plots_covered(PLOT, START, steps=offset + length)
    y2 = get_garden_plots_covered(PLOT, START, steps=offset + length * 2)
    a,b,c = get_coefficients(y0, y1, y2)
    x = steps // length
    return get_equation_value(a, b, c, x)

def get_coefficients(y0, y1, y2):
    '''
    y = ax2 + bx + c = 0
    x = 0, y0 = c
    x = 1, y1 = a + b + c
        => a + b = y1 - c 
        => a + b = y1 - y0
    x = 2, y2 = 4a + 2b + c 
        => 2(2a + b) = y2 - c 
        => 2(a + (a + b)) = y2 - y0
        => a + y1 - y0 = (y2 - y0)/2
        => a = (y2 - y0)/2 - (y1 - y0)

    a = (y2 - y0)/2 - (y1 - y0)
    b = (y1 - y0) - a = (y1 - y0) - (y2 - y0)/2 - (y1 - y0)
    c = y0
    '''
    a = (y2 - y0)//2 - (y1 - y0)
    b = (y1 - y0) - a
    c = y0
    return a,b,c

def get_equation_value(a, b, c, x):
    #y = ax2 + bx + c
    return a * x ** 2 + b * x + c


path = "21.Step_Counter\input.txt"
PLOT, START = get_puzzle(path)
rows, cols = len(PLOT), len(PLOT[0])

#Part 1
print(get_garden_plots_covered(PLOT, START, steps=64))

#Part 2
'''
Based on the logic and solution explained in this post:
https://www.reddit.com/r/adventofcode/comments/18nevo3/comment/keaiiq7/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
'''
print(get_garden_plots_covered_infinite(PLOT, START, steps=26501365))

