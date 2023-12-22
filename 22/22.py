class Brick:
    def __init__(self, start, end, label):
        self.start = list(map(int, start.split(',')))
        self.end = list(map(int, end.split(',')))
        self.label = label
        self.index = {"x":0, "y":1, "z":2}
        self.issingle = False
        self.orientation = self.find_orientation()
        self.volume = self.find_volume()
        

    def find_orientation(self):
        indices = {"x", "y", "z"}
        matching = set()
        # for index, coord1, coord2 in enumerate(zip(self.start, self.end)):
        #     if coord1 == coord2: print('yay')

        if self.start[0] == self.end[0]: #same x-coord
            matching.add("x")
        if self.start[1] == self.end[1]: #same y-coord
            matching.add("y")
        if self.start[2] == self.end[2]: #same z-coord
            matching.add("z")
        
        diff = indices - matching
        # print(self.start, self.end, matching, diff)
        if not diff:
            self.issingle = True
        else: return list(diff)[0]
    
    def find_volume(self):
        # start_x,start_y,start_z = self.start
        # end_x,end_y,end_z = self.end
        if self.issingle:   return 1
        # print(self.start, self.end, self.orientation)
        matching_index = self.index[self.orientation]
        return abs(self.start[matching_index] - self.end[matching_index]) + 1
    
    def compare_position(self, brick):
        matching_index = self.index[self.orientation]
        if self.start[matching_index] == brick.start[matching_index] or self.end[matching_index] == brick.end[matching_index]:
            return True
        return False 

    def display(self):
        print(self.start, self.end, self.orientation, self.volume, end = ", ")


def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)

def parse_input(file):
    BRICKS = [] #<brick no>:<start>, <end>
    for brick_no, line in enumerate(file):
        start, end = line.strip().split('~')
        # start_coordinates = start.split(',')
        # end_coordinates = end.split(',')
        # BRICKS.append((start.split(','), end.split(',')))
        BRICKS.append(Brick(start, end, brick_no))
        # BRICKS[brick_no] = ({'x':start_coordinates[0], 'y':start_coordinates[1], 'z':start_coordinates[2]},
        #                    {'x':end_coordinates[0], 'y':end_coordinates[1], 'z':end_coordinates[2]})
    # BRICKS = sorted(BRICKS, key=lambda brick: brick[1][2])
    return BRICKS

def get_safe_bricks(BRICKS):
    # overlapping = get_possible_merges(BRICKS)
    # return len(BRICKS) - merges
    overlaps = set()
    brick_count = len(BRICKS)
    sorted_bricks = sorted(BRICKS, key=lambda brick: brick.end[2])
    for brick1, brick2 in zip(BRICKS[:-1], BRICKS[1:]):
        if brick1.orientation == brick2.orientation:
            # and BRICKS[brick1].volume == BRICKS[brick2].volume:
            # print(brick1, BRICKS[brick1].start, BRICKS[brick1].end, brick2, BRICKS[brick2].start, BRICKS[brick2].end)
            # BRICKS[brick1].display()
            # BRICKS[brick2].display()
            # print('\n')
            if brick1.compare_position(brick2):
                overlaps.add(brick1.label)
                overlaps.add(brick2.label)
    overlaps.add(brick_count - 1)
    return len(overlaps)

path = "22\input.txt"
BRICKS = get_puzzle(path)
# print(BRICKS)
# for brick in BRICKS:
#     BRICKS[brick].display()
print(get_safe_bricks(BRICKS))