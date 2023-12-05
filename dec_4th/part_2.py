def get_winning_value(data):
    score, total_sum = 0, 0
    card_count = []

    for i in range(len(data)):
        card_count.append(1)

    for index, line in enumerate(data):
        winning_numbers = line.split('|')[0].split(':')[1].split()
        my_numbers = line.split('|')[1].split()
        count = len([number for number in my_numbers
                     if number in winning_numbers])
        score = pow(2, count - 1)

        for i in range(count):
            card_count[index + i + 1] += card_count[index]

        total_sum += score
        score, count = 0, 0

    return sum(card_count)


if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    data = [line for line in input_data if line]
    print(get_winning_value(data))
