import os
import re

class Solution:

    def __init__(self):
        self.ranges = []
        self.parse_input()

    def parse_input(self):
        with open(os.path.join(os.path.dirname(__file__),'input.txt'), 'r') as file:
            for line in file:
                self.ranges.append(tuple(int(x) for x in re.split(',|-',line.strip())))
            
    
    def part_one(self):
        fully_included_ranges = 0

        for range in self.ranges:
            range_1_min, range_1_max, range_2_min, range_2_max = range
            if (range_1_min >= range_2_min and range_1_max <= range_2_max) or (range_2_min >= range_1_min and range_2_max <= range_1_max):
                fully_included_ranges += 1
        
        print(fully_included_ranges)

    def part_two(self):
        overlapping_ranges = 0

        for range in self.ranges:
            range_1_min, range_1_max, range_2_min, range_2_max = range
            if (range_1_min <= range_2_max and range_2_min <= range_1_max):
                overlapping_ranges += 1
        
        print(overlapping_ranges)

if __name__ == '__main__':
    day4 = Solution()
    day4.part_one()
    day4.part_two()

#compose ranges

#find if ranges are inclued in other ranges