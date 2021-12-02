# input preprocessing
def process_input():
    with open("Advent/day1/input.txt") as file:
        input = file.readlines()
    return [int(i) for i in input]

# challenge 1
def count_measurement_increments(input):

    counter = 0

    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            counter += 1

    return counter

# challenge 2
def count_window_increments(input):

    window_size = 3
    counter = 0
    rolling_sum = sum(input[:window_size])

    for i in range(window_size, len(input)):
        prev_sum = rolling_sum
        rolling_sum -= input[i-window_size]
        rolling_sum += input[i]
        if rolling_sum > prev_sum:
            counter += 1

    return counter

