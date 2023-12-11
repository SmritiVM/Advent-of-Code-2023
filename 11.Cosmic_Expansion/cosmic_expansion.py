def get_puzzle(path):
    with open(path) as file:
        return parse_input(file)
    
def parse_input(file):
    #Generate a 2D matrix
    matrix = []
    for line in file:
        matrix.append(list(line.strip('\n')))

    # Find empty rows, columns and position of galaxies
    rows, cols = len(matrix), len(matrix[0])
    empty_rows, empty_cols = set(range(rows)), set(range(cols))
    galaxies, galaxy_number = {}, 1
    
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == "#":
                empty_rows.discard(x)
                empty_cols.discard(y)
                matrix[x][y] = galaxy_number
                galaxies[galaxy_number] = (x,y)
                galaxy_number += 1
    #Galaxies : {<galaxy_number>:(<x coord>, <y coord>)}
    return galaxies, empty_rows, empty_cols

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
    distance = x2 - x1 + y2 - y1

    # Check if empty row in between rows and add
    distance += add_expansion(x1, x2, EMPTY_ROWS, expansion)
    # Check if empty column in between column and add
    distance += add_expansion(y1, y2, EMPTY_COLS, expansion)

    return distance
    

def add_expansion(limit1, limit2, sequence, expansion):
    distance = 0
    for value in sequence:
        if limit1 < value < limit2: distance += expansion
    return distance

path = "11.Cosmic_Expansion\input.txt"
GALAXIES, EMPTY_ROWS, EMPTY_COLS = get_puzzle(path)

#Part 1
print(sum_of_lengths(GALAXIES, EMPTY_ROWS, EMPTY_COLS))

#Part 2
print(sum_of_lengths(GALAXIES, EMPTY_ROWS, EMPTY_COLS, expansion=1000000-1))
