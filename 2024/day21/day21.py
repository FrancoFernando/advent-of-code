from collections import deque
from functools import cache
from itertools import pairwise

class Solution:
    def __init__(self):
        self.codes = []
        self.numeric_keypad = {
            "0": [("2", "^"), ("A", ">")],
            "1": [("2", ">"), ("4", "^")],
            "2": [("0", "v"), ("1", "<"), ("3", ">"), ("5", "^")],
            "3": [("2", "<"), ("6", "^"), ("A", "v")],
            "4": [("1", "v"), ("5", ">"), ("7", "^")],
            "5": [("2", "v"), ("4", "<"), ("6", ">"), ("8", "^")],
            "6": [("3", "v"), ("5", "<"), ("9", "^")],
            "7": [("4", "v"), ("8", ">")],
            "8": [("5", "v"), ("7", "<"), ("9", ">")],
            "9": [("6", "v"), ("8", "<")],
            "A": [("0", "<"), ("3", "^")],
        }
        self.directional_keypad = {
            "^": [("A", ">"), ("v", "v")],
            "<": [("v", ">")],
            "v": [("<", "<"), ("^", "^"), (">", ">")],
            ">": [("v", "<"), ("A", "^")],
            "A": [("^", "<"), (">", "v")],
        }
        self.keypads = [self.numeric_keypad, self.directional_keypad]
        self.parse_input()

    def parse_input(self):
        with open("input.txt", "r") as file:
            self.codes = file.read().splitlines()

    def find_shortest_paths(self, start, end, keypad):
        q = deque([(start, [])])
        seen = {start}
        shortest_path_length = None
        shortest_path = []
        while q:
            current, path = q.popleft()
            if current == end:
                if shortest_path_length is None:
                    shortest_path_length = len(path)
                if len(path) == shortest_path_length:
                    shortest_path.append("".join(path + ["A"]))
                continue
            if shortest_path_length and len(path) >= shortest_path_length:
                continue
            for neighbor, direction in keypad[current]:
                seen.add(neighbor)
                q.append((neighbor, path + [direction]))
        return shortest_path

    @cache
    def dfs(self, sequence, level, keypad_type=0):
        current_keypad = self.keypads[keypad_type]
        result = 0
        sequence = "A" + sequence # Start from 'A' button
        for current_button, next_button in pairwise(sequence):
            paths = self.find_shortest_paths(current_button, next_button, current_keypad)
            if level == 0:
                result += min(map(len, paths))
            else:
                result += min(self.dfs(path, level - 1, 1) for path in paths)
        return result

    def part_one(self):
        return sum(self.dfs(code, 2) * int(code[:3]) for code in self.codes)

    def part_two(self):
        return sum(self.dfs(code, 25) * int(code[:3]) for code in self.codes)
       

if __name__ == '__main__':
    solution = Solution()
    print(f"Part 1: {solution.part_one()}")
    print(f"Part 2: {solution.part_two()}")
