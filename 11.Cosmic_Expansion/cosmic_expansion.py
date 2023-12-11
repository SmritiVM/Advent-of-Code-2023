from collections import deque
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Generate a 2D matrix
    matrix = []
    for line in file:
        matrix.append(list(line.strip('\n')))
      
    # Get all empty row and column indices
    # Get rows
    empty_rows = get_empty_rows(matrix)

    #Transpose matrix to get empty columns
    transpose = get_transpose(matrix)
    empty_columns = get_empty_rows(transpose)

    #Replace all galaxies with numbers and get their coordinates
    galaxies = find_galaxies(matrix)
    return galaxies, empty_rows, empty_columns

def get_empty_rows(matrix):
    # Get poisitions of empty rows
    empty_rows = []
    for index, row in enumerate(matrix):
        if '#' not in row:
            empty_rows.append(index)
    return empty_rows


def get_transpose(matrix):
    transpose = [[0 for x in range(len(matrix))] for y in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose[i][j] = matrix[j][i]
    return transpose

def find_galaxies(matrix):
    galaxies = {}
    galaxy_number = 1
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == '#':
                matrix[x][y] = galaxy_number
                galaxies[galaxy_number] = (x,y)
                galaxy_number += 1
    return galaxies

def sum_of_lengths(GALAXIES, EMPTY_ROWS, EMPTY_COLS, expansion=1):
    total = 0
    galaxy_count = len(GALAXIES)
    for galaxy1 in range(1, galaxy_count + 1):
        for galaxy2 in range(galaxy1 + 1, galaxy_count + 1):
            total += find_distance(galaxy1, galaxy2, GALAXIES, EMPTY_ROWS, EMPTY_COLS, expansion)
    return total



def find_distance(galaxy1, galaxy2, GALAXIES, EMPTY_ROWS, EMPTY_COLS, expansion):
    x1, y1 = GALAXIES[galaxy1]
    x2, y2 = GALAXIES[galaxy2]

    # Setting x1 and y1 as min coordinates
    if x1 > x2: x1, x2 = x2, x1
    if y1 > y2: y1, y2 = y2, y1
    x_diff, y_diff = x2 - x1, y2 - y1

    # Check if empty row in between rows
    for row in EMPTY_ROWS:
        if x1 < row < x2:
            x_diff += expansion
    
    
    # Check if empty column in between columns
    for column in EMPTY_COLS:
        if y1 < column < y2:
            y_diff += expansion

    return x_diff + y_diff
    
    

path = "11.Cosmic_Expansion\input.txt"
GALAXIES, EMPTY_ROWS, EMPTY_COLS = get_puzzle(path)

#Part 1
print(sum_of_lengths(GALAXIES, EMPTY_ROWS, EMPTY_COLS))

#Part 2
print(sum_of_lengths(GALAXIES, EMPTY_ROWS, EMPTY_COLS, expansion=1000000-1))
