from collections import defaultdict, deque
from copy import deepcopy
class Brick:
    def __init__(self, start, end, label):
        self.start = list(map(int, start.split(',')))
        self.end = list(map(int, end.split(',')))
        self.label = label
        self.xy_range = self.find_xy_range()
        self.height = self.end[2] - self.start[2] + 1

    def find_xy_range(self):
        return [(x, y) for x in range(self.start[0], self.end[0] + 1)
                for y in range(self.start[1], self.end[1] + 1)]


def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)

def parse_input(file):
    BRICKS = []
    for brick_no, line in enumerate(file):
        start, end = line.strip().split('~')
        BRICKS.append(Brick(start, end, brick_no))
    BRICKS = sorted(BRICKS, key=lambda brick: brick.start[2]) #sorting based on z
    return BRICKS

def get_safe_bricks(BELOW, brick_count):
    unsafe = set()
    for bricks in BELOW.values():
        if len(bricks) == 1: #If there is only 1 below, not safe to remove
            unsafe.update(bricks)
    return brick_count - len(unsafe)

def drop_bricks(BRICKS):
    above, below = defaultdict(set), defaultdict(set) #<brick>:[<list of bricks above/below>]
    zmap = defaultdict(lambda: defaultdict(lambda: ".")) #<height>:{<x,y>:< . /brick label>}
    for brick in BRICKS:
        current_height = brick.start[2] #z coord of start
        while current_height > 1 and all(zmap[current_height - 1][point] == "." for point in brick.xy_range):
            current_height -= 1 #drop the brick as long as all points covered by it are empty
        
        
        #Finding the bricks below the current brick
        bricks_below = set()
        for point in brick.xy_range:
            space = zmap[current_height - 1][point]
            if space != ".": #i.e another brick
                bricks_below.add(space)
        
        for support_brick in bricks_below:
            above[support_brick].add(brick.label)
            below[brick.label].add(support_brick)

        #Setting all the points with brick label after dropping
        for point in brick.xy_range:
            for offset in range(brick.height):
                zmap[current_height + offset][point] = brick.label
    return above, below

def get_sum_falling(ABOVE, BELOW, brick_count):
    total = 0
    for brick_no in range(brick_count):
        total += find_falling_count(brick_no, ABOVE, BELOW)
    return total  

def find_falling_count(brick_no, ABOVE, BELOW):
    above, below = deepcopy(ABOVE), deepcopy(BELOW)
    queue = deque([brick_no]) 
    falling = 0
    while queue:
        brick = queue.popleft()
        falling += 1
        for top in above[brick]:
            if brick in below[top]: below[top].remove(brick)
            if len(below[top]) == 0: #if there is nothing to support it, find the bricks that will disintegrate if top falls
                queue.append(top)
    return falling - 1 #not counting the original brick at the beginning of the queue


path = "22.Sand_Slabs\input.txt"
BRICKS = get_puzzle(path)
brick_count = len(BRICKS)
print(brick_count)
ABOVE, BELOW = drop_bricks(BRICKS)

#Part 1
print(get_safe_bricks(BELOW, brick_count))

#Part 2
print(get_sum_falling(ABOVE, BELOW, brick_count))

'''
    above   below
A -> B, C
B -> D, E   A
C -> D, E   A
D -> F      B, C
E -> F      B, C
F -> G      D, E
falling -> 0


'''