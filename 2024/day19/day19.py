from functools import lru_cache

class Solution:
    def __init__(self):
        self.towel_patterns = []
        self.designs = []
        self.parse_input()

    def parse_input(self):
        with open('input.txt', 'r') as file:
            lines = file.readlines()
            self.towel_patterns = tuple(lines[0].strip().split(', '))  # Convert to tuple for hashing
            self.designs = [line.strip() for line in lines[2:]]

    @lru_cache(maxsize=None)
    def can_make_design(self, remaining):
        if not remaining:
            return True
        for pattern in self.towel_patterns:
            if remaining.startswith(pattern):
                if self.can_make_design(remaining[len(pattern):]):
                    return True
        return False

    def count_possible_designs(self):
        return sum(self.can_make_design(design) for design in self.designs)

    def part_one(self):
        possible_designs = self.count_possible_designs()
        return possible_designs
    
    @lru_cache(maxsize=None)
    def count_ways_to_make_design(self, remaining):
        if not remaining:
            return 1  # One way to make an empty design
        
        total_ways = 0
        for pattern in self.towel_patterns:
            if remaining.startswith(pattern):
                total_ways += self.count_ways_to_make_design(remaining[len(pattern):])
        
        return total_ways

    def part_two(self):
        total_ways = sum(self.count_ways_to_make_design(design) for design in self.designs)
        return total_ways

if __name__ == '__main__':
    solution = Solution()
    print(f"Part One: {solution.part_one()}")
    print(f"Part Two: {solution.part_two()}")
