# part_sum = 0
def sum_of_parts(schematic):
    part_sum = 0
    row_limit, col_limit = len(schematic), len(schematic[0]) - 1
    print(row_limit, col_limit)
    current_num, is_partnum = 0, False
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
                    #Top
                    elif (x != 0) and (not schematic[x - 1][y].isalnum() and schematic[x - 1][y] != '.'):
                        is_partnum = True
                    #Top right
                    elif (x != 0) and (y != col_limit - 1) and (not schematic[x - 1][y + 1].isalnum() and schematic[x - 1][y + 1] != '.'):
                        is_partnum = True
                    #Left
                    elif (y != 0) and (not schematic[x][y - 1].isalnum() and schematic[x][y - 1] != '.'):
                        is_partnum = True
                    #Right
                    elif (y != col_limit - 1) and (not schematic[x][y + 1].isalnum() and schematic[x][y + 1] != '.'):
                        is_partnum = True
                    #Bottom left
                    elif (x != row_limit - 1) and (y != 0) and (not schematic[x + 1][y - 1].isalnum() and schematic[x + 1][y - 1] != '.'):
                        is_partnum = True
                    #Bottom
                    elif (x != row_limit - 1) and (not schematic[x + 1][y].isalnum() and schematic[x + 1][y] != '.'):
                        is_partnum = True
                    #Bottom right
                    elif (x != row_limit - 1) and (y != col_limit - 1) and (not schematic[x + 1][y + 1].isalnum() and schematic[x + 1][y + 1] != '.'):
                        is_partnum = True
                    
            
            #Check if it is the last digit
            if (y < row_limit - 1 and not schematic[x][y + 1].isdigit()) or (y == row_limit - 1):
                #Check if it can be added to part sum
                if is_partnum: part_sum += current_num
                #Reset variables
                current_num = 0
                is_partnum = False
            

    return part_sum   
                 

            # #Check if it is a symbol
            # if not schematic[x][y].isalnum() or not schematic[x][y] == '.':
            #     #Checking all adjacent indices
            #     #Top left
            #     if x != 0 and y != 0 and schematic[x - 1][y - 1].isdigit():


with open ("3. Gear Ratios\input.txt") as input:
    schematic = input.readlines()
    print(sum_of_parts(schematic))