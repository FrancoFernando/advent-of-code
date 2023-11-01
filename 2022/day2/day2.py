import os

class Solution:

    score_per_shape = {'rock':1, 'paper':2, 'scissors':3}
    score_per_outcome = {'lose':0, 'draw':3, 'win':6}
    opponent_encoding = {'A':'rock', 'B':'paper','C':'scissors'}
    our_encoding = {'X':'rock', 'Y':'paper','Z':'scissors'}
    outcome_encoding = {'X':'lose', 'Y':'draw','Z':'win'}
    rules = {'rock-rock':'draw','rock-paper':'win','rock-scissors':'lose',
            'paper-rock':'lose','paper-paper':'draw','paper-scissors':'win',
            'scissors-rock':'win','scissors-paper':'lose','scissors-scissors':'draw'}

    inverted_rules = {'rock-draw':'rock','rock-win':'paper','rock-lose':'scissors',
            'paper-lose':'rock','paper-draw':'paper','paper-win':'scissors',
            'scissors-win':'rock','scissors-lose':'paper','scissors-draw':'scissors'}

    def __init__(self) -> None:
        self.input = self.parse_input()

    def parse_input(self):
        with open(os.path.join(os.path.dirname(__file__),'input.txt'), 'r') as file:
            return [line.split() for line in file]

    def part_one(self):
        result = 0

        for line in self.input:
            opponent, our = line
            opponent, our = self.opponent_encoding[opponent], self.our_encoding[our]
            match = opponent+'-'+our
            outcome = self.rules[match]
            result += self.score_per_shape[our]
            result += self.score_per_outcome[outcome]

        print(result)

    def part_two(self):
        result = 0

        for line in self.input:
            opponent, outcome = line
            opponent, outcome = self.opponent_encoding[opponent], self.outcome_encoding[outcome]
            match = opponent+'-'+outcome
            our = self.inverted_rules[match]
            result += self.score_per_shape[our]
            result += self.score_per_outcome[outcome]

        print(result)

if __name__ == '__main__':

    day2 = Solution()
    day2.part_one()
    day2.part_two()


