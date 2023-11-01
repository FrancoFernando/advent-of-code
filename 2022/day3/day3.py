import os
import string

class Solution:

    priority = {char:index+1 for index, char in enumerate(string.ascii_letters)} 

    def __init__(self) -> None:
        self.rucksacks = self.parse_input()

    def parse_input(self):

        rucksacks = []
        with open(os.path.join(os.path.dirname(__file__),'input.txt'), 'r') as file:
            for line in file:
                rucksacks.append(line.strip())
        return rucksacks

    def part_one(self):

        priorities = 0

        for rucksack in self.rucksacks:
            compartment_1 = set(rucksack[:len(rucksack)//2])
            compartment_2 = set(rucksack[len(rucksack)//2:])
            common_items = compartment_1.intersection(compartment_2)
            priorities += self.priority[list(common_items)[0]]
        
        print(priorities)

    def part_two(self):

        priorities = 0

        for index in range(0, len(self.rucksacks), 3):
            rucksack_1 = set(self.rucksacks[index])
            rucksack_2 = set(self.rucksacks[index+1])
            rucksack_3 = set(self.rucksacks[index+2])
            common_items = rucksack_1.intersection(rucksack_2, rucksack_3)
            priorities += self.priority[list(common_items)[0]]

        print(priorities)


if __name__ == '__main__':
    day3 = Solution() 
    day3.part_one()
    day3.part_two()
        