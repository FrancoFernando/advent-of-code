def process_input():
    with open("Advent/day7/input.txt", "r") as file:
        data = file.read()
        positions = [int(num) for num in data.split(",")]
    return positions

def min_fuel(input):

    n = len(input)
    input.sort()
  
    if n % 2 == 0:
        median1 = input[n//2]
        median2 = input[n//2 - 1]
        median = (median1 + median2)//2
    else:
        median = input[n//2]

    min_fuel = sum(abs(median - pos) for pos in input)
    return min_fuel

from collections import Counter

def partial_sum(n):
    return n * (n + 1) // 2

def fuel(pos_to_frequency, current_pos):
    return sum(partial_sum(abs(pos - current_pos)) * freq for pos, freq in pos_to_frequency.items())

def min_fuel_part2(input):

    pos_to_frequency = dict(Counter(input))

    min_pos = min(input)
    max_pos = max(input)
    min_fuel = fuel(pos_to_frequency, min_pos)
    max_fuel = fuel(pos_to_frequency, max_pos)

    while min_pos < max_pos:
        if min_fuel < max_fuel:
            max_pos = (max_pos + min_pos) // 2
            max_fuel = fuel(pos_to_frequency, max_pos)
        else:
            min_pos = (max_pos + min_pos + 1) // 2
            min_fuel = fuel(pos_to_frequency, min_pos)

    return min_fuel

