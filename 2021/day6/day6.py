def process_input():
    with open("Advent/day6/input.txt") as file:
        input = [line.split(",") for line in file]
    return [int(i) for i in input[0]]

def population(input):

    frequency_map = [0]*9

    for fish in input:
        frequency_map[fish] += 1

    for day in range(256):

        zeros = frequency_map[0]

        for i in range(1,9):
            frequency_map[i-1] = frequency_map[i]

        frequency_map[8] = 0
        frequency_map[6] += zeros
        frequency_map[8] += zeros

    return sum(frequency_map)

