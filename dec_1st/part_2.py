'''
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: 
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''

num_dict = {
    'one': 'on1e',
    'two': 'tw2o',
    'three': 'thr3ee',
    'four': 'fo4ur',
    'five': 'fi5ve',
    'six': 'si6x',
    'seven': 'sev7en',
    'eight': 'eig8ht',
    'nine': 'ni9ne'
}

total = 0

with open('input.txt', 'r') as file:
    input_data = file.read().split()

for line in input_data:
    for key, value in num_dict.items():
        if key in line:
            line = line.replace(key, str(value))

    line_numbers = []

    for char in line:
        try:
            char = int(char)
            line_numbers.append(str(char))
        except:
            pass

    if len(line_numbers) < 2:
        line_numbers = ''.join([line_numbers[0], line_numbers[0]])
        print(line_numbers)
        total += int(line_numbers)

    else:
        line_numbers = ''.join([line_numbers[0], line_numbers[-1]])
        print(line_numbers)
        total += int(line_numbers)

print(total)