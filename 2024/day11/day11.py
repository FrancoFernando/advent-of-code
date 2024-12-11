from collections import Counter

class Solution:

    def __init__(self):
        self.stones = []
        self.parse_input()

    def parse_input(self):

        with open('input.txt', 'r') as file:
            data = file.read()
        self.stones = [int(x) for x in data.strip().split()]
        print(self.stones)

    def transform_stone(self, stone):
        # Rule 1: If the stone is 0, replace with 1
        if stone == 0:
            return [1]
        
        # Rule 2: If the stone has an even number of digits, split it
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            mid = len(stone_str) // 2
            return [int(stone_str[:mid]), int(stone_str[mid:])]
        
        # Rule 3: Multiply by 2024
        return [stone * 2024]

    def part_one(self):
        stones = self.stones
        for _ in range(25):
            new_stones = []
            for stone in stones:
                new_stones.extend(self.transform_stone(stone))
            stones = new_stones
        return len(stones)
    
    def iterate_blink(self, counter):
        new_counter = Counter()
        for x, count in counter.items():
            for new_x in self.transform_stone(x):
                new_counter[new_x] += count
        return new_counter

    def part_two(self):
        counter = Counter(self.stones)
        for _ in range(75):
            counter = self.iterate_blink(counter)
        
        return sum(counter.values())

if __name__ == '__main__':
    day1 = Solution() 
    print(day1.part_one())
    print(day1.part_two())