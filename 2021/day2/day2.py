# input preprocessing
def process_input():
    with open("Advent/day2/input.txt") as file:
        input = [line.split() for line in file]
    return input

# challenge 1
def multiply_final_position(input):

    horizontal = 0
    vertical = 0

    for move, unit in input:
        if move == "forward":
            horizontal += int(unit)
        elif move == "up":
            vertical -= int(unit)
        else:
            vertical += int(unit)

    return horizontal * vertical

# challenge 2
def multiply_final_position_with_aim(input):

    aim = 0
    horizontal = 0
    vertical = 0

    for move, unit in input:
        if move == "forward":
            horizontal += int(unit)
            vertical += aim * int(unit)
        elif move == "up":
            aim -= int(unit)
        else:
            aim += int(unit)

    return horizontal * vertical
