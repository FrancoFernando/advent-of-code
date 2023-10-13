score_per_shape = {'rock':1, 'paper':2, 'scissors':3}
score_per_outcome = {'lose':0, 'draw':3, 'win':6}
opponent_encoding = {'A':'rock', 'B':'paper','C':'scissors'}
our_encoding = {'X':'rock', 'Y':'paper','Z':'scissors'}
outcome_encoding = {'X':'lose', 'Y':'draw','Z':'win'}
rules = {'rock-rock':'draw','rock-paper':'win','rock-scissors':'lose',
         'paper-rock':'lose','paper-paper':'draw','paper-scissors':'win',
         'scissors-rock':'win','scissors-paper':'lose','scissors-scissors':'draw'}

def parse_input():
    with open("2022/day2/input.txt", 'r') as file:
        return [line.split() for line in file]

def part_one(input):
    result = 0

    for line in input:
        opponent, our = line
        opponent, our = opponent_encoding[opponent], our_encoding[our]
        match = opponent+'-'+our
        outcome = rules[match]
        result += score_per_shape[our]
        result += score_per_outcome[outcome]

    print(result)

if __name__ == '__main__':

    input = parse_input()
    part_one(input)


