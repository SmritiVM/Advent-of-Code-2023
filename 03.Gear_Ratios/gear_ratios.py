from collections import defaultdict

class Gear_Ratios:
    def __init__(self, schematic):
        self.schematic = schematic

        #Part 1 Variables
        self.part_sum = 0
        self.current_num, self.is_partnum = 0, False

        #Part 2 Variables
        self.gear_ratio_sum = 0
        self.adjacent = defaultdict(lambda: []) #{<pos of '*'>:[<adjacent part nums>]}
        self.symbol_position = tuple()

    def inspect_cell(self, x, y):
        '''
        Check if symbol
        If symbol => the current number can be a part num
        If symbol = '*' => the current number can be a gear part
        '''
        if self.is_symbol(x, y):
            self.is_partnum = True
            if self.schematic[x][y] == '*':
                self.symbol_position = (x, y)

    def is_symbol(self, x, y):
        '''
        Character that is not alphanumeric or '.' is a symbol
        '''
        return not self.schematic[x][y].isalnum() and self.schematic[x][y] != '.'
    
    def compute_sums(self):
        '''
        Returning answers for
        Part 1: Finding sum of parts
        Part 2: Finding sum of gear rations
        '''
        #Iteration limits
        row_limit, col_limit = len(schematic), len(schematic[0]) - 1
        
        #Checking the schematic index by index
        for x in range(row_limit):
            for y in range(col_limit):
                #Check if it is a digit
                if self.schematic[x][y].isdigit():
                    self.current_num = self.current_num * 10 + int(self.schematic[x][y])
                    #Check if it can be a part num
                    if not self.is_partnum:
                        # print(self.current_num)
                        #Check all adjacent cells for a symbol
                        neighbours = [[-1,-1], [-1,0], [-1,1],
                                      [0,-1], [0, 1],
                                      [1,-1], [1,0], [1,1]]
                        for dx, dy in neighbours:
                            if self.is_partnum: break
                            try: self.inspect_cell(x + dx, y + dy)
                            except: pass       
                
                    #Check if it is the last digit
                    if (y < col_limit - 1 and not self.schematic[x][y + 1].isdigit()) or (y == col_limit - 1):
                        #Check if it can be added to part sum
                        if self.is_partnum: 
                            self.part_sum += self.current_num
                            if self.symbol_position: self.adjacent[self.symbol_position].append(self.current_num)

                        #Reset variables
                        self.current_num = 0
                        self.is_partnum = False
                        self.symbol_position = tuple()
                
        for star in self.adjacent:
            if len(self.adjacent[star]) != 2:
                continue
            self.gear_ratio_sum += self.adjacent[star][0] * self.adjacent[star][1]

        return self.part_sum, self.gear_ratio_sum


with open ("03.Gear_Ratios\input.txt") as input:
    schematic = input.readlines()
    puzzle = Gear_Ratios(schematic)
    print(puzzle.compute_sums())