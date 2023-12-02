max_blue = 14
max_red = 12
max_green = 13
sum_possible_games = 0

with open('input.txt', 'r') as file:
    input_data = [line.strip() for line in file]

game_id = 1
for game in input_data:
    cubes = game.split(':')[1]
    hands = cubes.split(';')
    blue = 0
    red = 0
    green = 0

    for hand in hands:
        this_hand = [h.strip() for h in hand.split(',')]

        for set in this_hand:
            num, color = set.split(' ')
            if color == 'blue':
                if int(num) > blue:
                    blue = int(num)
            elif color == 'red':
                if int(num) > red:
                    red = int(num)
            elif color == 'green':
                if int(num) > green:
                    green = int(num)

    if blue <= max_blue and red <= max_red and green <= max_green:
        sum_possible_games += game_id

    game_id += 1

print(f"Sum of games possible: {sum_possible_games}")
