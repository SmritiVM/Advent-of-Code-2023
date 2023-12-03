from collections import defaultdict
#Find gear ratio => find a partnum and find another part_num before x + 1 or y + 1
def sum_of_parts(schematic):
    part_sum = 0
    gear_ratio_sum = 0
    row_limit, col_limit = len(schematic), len(schematic[0]) - 1
    current_num, is_partnum = 0, False
    adjacent = defaultdict(lambda: [])
    symbol_position = tuple()
    for x in range(row_limit):
        for y in range(col_limit):
            if schematic[x][y].isdigit():
                current_num = current_num * 10 + int(schematic[x][y])
                #Check if it can be added to part sum
                if not is_partnum:
                    #Check all adjacent cells for a symbol
                    #Top left
                    if (x != 0) and (y != 0) and (not schematic[x - 1][y - 1].isalnum() and schematic[x - 1][y - 1] != '.'):
                        is_partnum = True
                        if schematic[x - 1][y - 1] == '*':
                            symbol_position = (x - 1, y - 1)
                            
                    #Top
                    elif (x != 0) and (not schematic[x - 1][y].isalnum() and schematic[x - 1][y] != '.'):
                        is_partnum = True
                        if schematic[x - 1][y] == '*':
                            symbol_position = (x - 1, y)
                            
                    #Top right
                    elif (x != 0) and (y != col_limit - 1) and (not schematic[x - 1][y + 1].isalnum() and schematic[x - 1][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x - 1][y + 1] == '*':
                            symbol_position = (x - 1, y + 1)
                            
                    #Left
                    elif (y != 0) and (not schematic[x][y - 1].isalnum() and schematic[x][y - 1] != '.'):
                        is_partnum = True
                        if schematic[x][y - 1] == '*':
                            symbol_position = (x, y - 1)
                            
                    #Right
                    elif (y != col_limit - 1) and (not schematic[x][y + 1].isalnum() and schematic[x][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x][y + 1] == '*':
                            symbol_position = (x, y + 1)
                        
                    #Bottom left
                    elif (x != row_limit - 1) and (y != 0) and (not schematic[x + 1][y - 1].isalnum() and schematic[x + 1][y - 1] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y - 1] == '*':
                            symbol_position = (x + 1, y - 1)
                    
                    #Bottom
                    elif (x != row_limit - 1) and (not schematic[x + 1][y].isalnum() and schematic[x + 1][y] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y] == '*':
                            symbol_position = (x + 1, y)
                
                    #Bottom right
                    elif (x != row_limit - 1) and (y != col_limit - 1) and (not schematic[x + 1][y + 1].isalnum() and schematic[x + 1][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y + 1] == '*':
                            symbol_position = (x + 1, y + 1)
                    
            
            #Check if it is the last digit
            if (y < row_limit - 1 and not schematic[x][y + 1].isdigit()) or (y == row_limit - 1):
                #Check if it can be added to part sum
                if is_partnum: 
                    part_sum += current_num
                    if symbol_position: adjacent[symbol_position].append(current_num)

                #Reset variables
                current_num = 0
                is_partnum = False
                symbol_position = tuple()
            
    print(adjacent)
    return part_sum   


with open ("3. Gear Ratios\sampleinput.txt") as input:
    schematic = input.readlines()
    print(sum_of_parts(schematic))