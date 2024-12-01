from collections import Counter

class Solution:

    def __init__(self):
        self.left = []
        self.right = []
        self.parse_input()

    def parse_input(self):

        with open('input.txt', 'r') as file:
            
            for line in file:
                
                num1, num2 = line.split()
                self.left.append(int(num1))
                self.right.append(int(num2))

    def part_one(self):
        
        sorted_left = sorted(self.left)
        sorted_right= sorted(self.right)
        
        differences = [abs(a - b) for a, b in zip(sorted_left, sorted_right)]
        
        total_difference = sum(differences)
        print(total_difference)
        return total_difference

    def part_two(self):
        similarity = 0
        right_counter = Counter(self.right)

        for left in self.left:
            similarity += right_counter[left] * left

        print(similarity)
        return similarity


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()