def get_winning_value(line):
    count = 0

    winning_numbers = line.split('|')[0].split(':')[1].split()
    my_numbers = line.split('|')[1].split()

    count = len([number for number in my_numbers if number in winning_numbers])

    if count > 0:
        return pow(2, (count - 1))
    else:
        return 0


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    sum = 0
    for line in input_data:
        sum += get_winning_value(line)
    print(sum)
