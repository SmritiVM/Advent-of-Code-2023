from collections import deque
def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Generate a 2D matrix
    matrix = []
    for line in file:
        matrix.append(list(line.strip('\n')))
    print(len(matrix), len(matrix[0]))
    
    # Replace all empty rows and columns
    # Replace rows
    expand_rows(matrix)
    #Transpose matrix to replace columns
    transpose = get_transpose(matrix)
    expand_rows(transpose)
    #Get back original matrix
    matrix = get_transpose(transpose)
    
    # print(*matrix, sep = '\n')
    # print(len(matrix), len(matrix[0]))

    #Replace all galaxies with numbers and get their coordinates
    galaxies = find_galaxies(matrix)
    return matrix, galaxies

def expand_rows(matrix):
    # Get poisitions of empty rows
    empty_rows = deque([])
    for index, row in enumerate(matrix):
        if '#' not in row:
            empty_rows.append(index)
    #Replace empty rows
    while empty_rows:
        index = empty_rows.popleft()
        matrix.insert(index + 1, matrix[index])
        #Modifying remaining indices
        for i in range(len(empty_rows)):
            empty_rows[i] += 1

    # print(*matrix, sep = '\n')
    # print(len(matrix), len(matrix[0]))

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

def sum_of_lengths(MATRIX, GALAXIES):
    total = 0
    galaxy_count = len(GALAXIES)
    for galaxy1 in range(1, galaxy_count + 1):
        for galaxy2 in range(galaxy1 + 1, galaxy_count + 1):
            total += find_distance(galaxy1, galaxy2, GALAXIES)
    return total

def find_distance(galaxy1, galaxy2, GALAXIES):
    x1, y1 = GALAXIES[galaxy1]
    x2, y2 = GALAXIES[galaxy2]
    return abs(x1 - x2) + abs(y1 - y2)

path = "11\input.txt"
MATRIX, GALAXIES = get_puzzle(path)
# print(*MATRIX, sep = '\n')
# print(GALAXIES)
print(sum_of_lengths(MATRIX, GALAXIES))
