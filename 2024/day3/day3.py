import re

class Solution:

    def parse_input(self, pattern):
        
        valid_instructions = []

        with open("input.txt", 'r') as file:
            content = file.read()
            matches = re.findall(pattern, content)

            for match in matches:
                instruction = f"mul({match[0]},{match[1]})"
                valid_instructions.append(instruction)
                print(match)

        return valid_instructions     

    def part_one(self):
        # Regular expression pattern to match valid mul instructions
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        valid_instructions = self.parse_input(pattern)

        result = 0
        for instruction in valid_instructions:
            numbers = instruction[4:-1].split(',')
            result += int(numbers[0]) * int(numbers[1])

        print(result)
        return result

    def part_two(self):
        
        # Regular expression pattern to match valid mul, do, don't instructions
        pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
        valid_instructions = self.parse_input(pattern)

        result = 0
        enable_instructions = True
        for instruction in valid_instructions:
            instruction_name = instruction[:3]
            if instruction_name == "mul" and enable_instructions:
                numbers = instruction[4:-1].split(',')
                result += int(numbers[0]) * int(numbers[1])
            elif instruction_name == "don":
                enable_instructions = False
            elif instruction_name == "do(":
                enable_instructions = True

        print(result)
        return result


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    #day1.part_two()