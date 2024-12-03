import re

class Solution:

    def parse_input(self, pattern):
        
        valid_instructions = []

        with open("input.txt", 'r') as file:
            content = file.read()
            matches = re.findall(pattern, content)
            valid_instructions.extend(matches)
            
        return valid_instructions     

    def part_one(self):
        # Regex pattern to match valid mul instructions
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        valid_instructions = self.parse_input(pattern)

        result = 0
        for numbers in valid_instructions:
            result += int(numbers[0]) * int(numbers[1])

        print(result)
        return result

    def part_two(self):   
        # Regex pattern to match valid mul, do, don't instructions
        pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
        valid_instructions = self.parse_input(pattern)

        result = 0
        instructions_enabled = True
        for instruction in valid_instructions:
            if instruction.startswith('mul') and instructions_enabled:
                numbers = instruction[4:-1].split(',')
                result += int(numbers[0]) * int(numbers[1])
            elif instruction == "don't()":
                instructions_enabled = False
            elif instruction == "do()":
                instructions_enabled = True

        print(result)
        return result


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()
    