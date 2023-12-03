from collections import defaultdict
#Find gear ratio => find a partnum and find another part_num before x + 1 or y + 1
def sum_of_parts(schematic):
    part_sum = 0
    gear_ratio_sum = 0
    row_limit, col_limit = len(schematic), len(schematic[0]) - 1
    print(row_limit, col_limit)
    current_num, is_partnum = 0, False
    gear_ratio, is_gear_part, is_first_part, is_second_part = 1, False, False, False
    prev_gear_x = prev_gear_y = -1
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
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Top
                    elif (x != 0) and (not schematic[x - 1][y].isalnum() and schematic[x - 1][y] != '.'):
                        is_partnum = True
                        if schematic[x - 1][y] == '*':
                            symbol_position = (x - 1, y)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Top right
                    elif (x != 0) and (y != col_limit - 1) and (not schematic[x - 1][y + 1].isalnum() and schematic[x - 1][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x - 1][y + 1] == '*':
                            symbol_position = (x - 1, y + 1)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Left
                    elif (y != 0) and (not schematic[x][y - 1].isalnum() and schematic[x][y - 1] != '.'):
                        is_partnum = True
                        if schematic[x][y - 1] == '*':
                            symbol_position = (x, y - 1)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Right
                    elif (y != col_limit - 1) and (not schematic[x][y + 1].isalnum() and schematic[x][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x][y + 1] == '*':
                            symbol_position = (x, y + 1)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Bottom left
                    elif (x != row_limit - 1) and (y != 0) and (not schematic[x + 1][y - 1].isalnum() and schematic[x + 1][y - 1] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y - 1] == '*':
                            symbol_position = (x + 1, y - 1)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Bottom
                    elif (x != row_limit - 1) and (not schematic[x + 1][y].isalnum() and schematic[x + 1][y] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y] == '*':
                            symbol_position = (x + 1, y)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    #Bottom right
                    elif (x != row_limit - 1) and (y != col_limit - 1) and (not schematic[x + 1][y + 1].isalnum() and schematic[x + 1][y + 1] != '.'):
                        is_partnum = True
                        if schematic[x + 1][y + 1] == '*':
                            symbol_position = (x + 1, y + 1)
                            is_gear_part = True
                            if not is_first_part: is_first_part = True
                            else: is_second_part = True
                    
            
            #Check if it is the last digit
            if (y < row_limit - 1 and not schematic[x][y + 1].isdigit()) or (y == row_limit - 1):
                #Check if it can be added to part sum
                if is_partnum: 
                    part_sum += current_num
                    if symbol_position: adjacent[symbol_position].append(current_num)
                    # #Check if second part
                    # if is_second_part:
                    #     # print(prev_gear_x, x, prev_gear_y, y)
                    #     # print(current_num)
                    #     if (prev_gear_x <= x <= prev_gear_x + 2):
                    #         print(current_num)
                    #         #Multiply and reset
                    #         gear_ratio *= current_num
                    #         gear_ratio_sum += gear_ratio

                    #     gear_ratio, is_first_part, is_second_part = 1, False, False
                    #     prev_gear_x, prev_gear_y = x, y


                    # #Check if first part
                    # elif is_first_part:
                    #     gear_ratio *= current_num
                    #     prev_gear_x, prev_gear_y = x, y


                #Reset variables
                current_num = 0
                is_partnum = False
                symbol_position = tuple()
            
    print(adjacent)
    return part_sum   
                 

            # #Check if it is a symbol
            # if not schematic[x][y].isalnum() or not schematic[x][y] == '.':
            #     #Checking all adjacent indices
            #     #Top left
            #     if x != 0 and y != 0 and schematic[x - 1][y - 1].isdigit():


with open ("3. Gear Ratios\sampleinput.txt") as input:
    schematic = input.readlines()
    print(sum_of_parts(schematic))