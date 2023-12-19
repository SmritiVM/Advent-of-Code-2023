# import re
import regex as re
def calibration_value(line):
    # digits = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))', line)
    digits = re.findall('one|two|three|four|five|six|seven|eight|nine|[1-9]', line, overlapped=True)
    first_digit, last_digit = digit_value(digits[0]), digit_value(digits[-1])         
    return int(first_digit + last_digit)

def digit_value(element):
    if element.isdigit(): return element
    name2digit = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    return name2digit[element]

def sum_of_calibrations(file):
    sum = 0
    for line in file:
        sum += calibration_value(line)
    return sum
        
with open("01.Trebuchet\input1.txt") as file:
    print(sum_of_calibrations(file))