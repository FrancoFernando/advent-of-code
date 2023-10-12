class Solution:

    def __init__(self):
        self.calories = []
        self.parse_input()

    def parse_input(self):
        with open("2022/day1/input.txt", 'r') as file:

            self.calories.append(0)
            
            for line in file:
                
                if line.strip():
                    self.calories[-1] += int(line.strip())
                else:
                    self.calories.append(0)
    
    def part_one(self):
        result = max(self.calories)
        print(result)

    def part_two(self):
        result = sum(sorted(self.calories, reverse=True)[:3])
        print(result)

if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()
            
