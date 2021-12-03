# input preprocessing
def process_input():
    with open("Advent/day3/input.txt") as file:
        input = file.read().split()
    return input

# challenge 1
def power_consumption(input):

    binary_size = len(input[0])
    zero_frequency = [0]*binary_size
    one_frequency = [0]*binary_size

    for entry in input:
        for pos in range(binary_size):
            if entry[binary_size-pos-1] == "1":
                one_frequency[binary_size-pos-1] += 1
            else:
                zero_frequency[binary_size-pos-1] += 1

    gamma = 0
    epsilon = 0

    for pos in range(binary_size):
        if one_frequency[pos] > zero_frequency[pos]:
            gamma |= (1 << binary_size-pos-1)
        else:
            epsilon |= (1 << binary_size-pos-1)

    return gamma * epsilon

# challenge 2
def rating(input, type):

    considered = input
    pos = 0

    while len(considered) > 1:
        zero_frequency = 0
        one_frequency = 0

        for entry in considered:
            if entry[pos] == "1":
                one_frequency += 1
            else:
                zero_frequency += 1     

        if zero_frequency > one_frequency:
            considered = [num for num in considered if num[pos] == ("0" if type == "oxygen" else "1")]
        else:
            considered = [num for num in considered if num[pos] == ("1" if type == "oxygen" else "0")]

        pos += 1

    return int(considered[0],2)

def life_support_rating(input):

    return rating(input,"oxygen") * rating(input,"c02")

