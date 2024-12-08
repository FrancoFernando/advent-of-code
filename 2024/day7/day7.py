from itertools import product

class Solution:

    def __init__(self):
        self.results = []
        self.operands = []
        self.invalid_operations = []
        self.part1_result = 0
        self.parse_input()

    def parse_input(self):
        
        with open("input.txt", 'r') as file:
           for line in file:
                parts = line.strip().split(': ')
                self.results.append(int(parts[0]))
                self.operands.append([int(x) for x in parts[1].split()])

    def evaluate_expression(self, operators, values):
        result = values[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += values[i+1]
            elif op == '*':
                result *= values[i+1]
            else: # op == '||'
                result = int(str(result) + str(values[i+1]))
        return result

    def part_one(self): 
        
        total = 0
        for i in range(len(self.operands)):
            
            operators_combos = list(product(['+', '*'], repeat=len(self.operands[i])-1))
    
            for operators in operators_combos:
                if self.evaluate_expression(operators, self.operands[i]) == self.results[i]:
                    total += self.results[i]
                    break
            else:
                self.invalid_operations.append(i)
                
        self.part1_result = total
        print(total)
        return total
        
    def part_two(self):
        total = 0
        for i in self.invalid_operations:
            
            operators_combos = list(product(['+', '*', '||'], repeat=len(self.operands[i])-1))

            for operators in operators_combos:
                if self.evaluate_expression(operators, self.operands[i]) == self.results[i]:
                    total += self.results[i]
                    break
        
        total += self.part1_result
        print(total)
        return total
        
if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()