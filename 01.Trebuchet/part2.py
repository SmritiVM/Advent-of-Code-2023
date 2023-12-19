def calibration_value(line):
    name2digit = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    valid_digits = list(name2digit.keys()) +  list(name2digit.values())
    first_digit = last_digit = ''
    first_digit_pos, last_digit_pos = len(line), -1
    for digit in valid_digits:
        pos = line.find(digit, 0)
        while pos != -1:
            if pos < first_digit_pos:
                first_digit_pos = pos
                if digit.isdigit(): first_digit = digit
                else: first_digit = name2digit[digit]
            if pos > last_digit_pos:
                last_digit_pos = pos
                if digit.isdigit(): last_digit = digit
                else: last_digit = name2digit[digit]
            pos = line.find(digit, pos + 1)
            
    return int(first_digit + last_digit)

def sum_of_calibrations(file):
    sum = 0
    for line in file:
        sum += calibration_value(line)
    return sum
        
with open("01.Trebuchet\input1.txt") as file:
    print(sum_of_calibrations(file))