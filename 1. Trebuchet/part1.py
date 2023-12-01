def calibration_value(line):
    first_digit = last_digit = ''
    for char in line:
        if char.isdigit():
            if not first_digit:
                first_digit = char
            last_digit = char
    return int(first_digit + last_digit)

def sum_of_calibrations(file):
    sum = 0
    for line in file:
        sum += calibration_value(line)
    return sum
        
with open("1\input1.txt") as file:
    print(sum_of_calibrations(file))