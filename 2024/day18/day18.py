from collections import deque

class Solution:
    def __init__(self):
        self.corrupted = []
        self.parse_input()
        self.max_x = 70
        self.max_y = 70

    def parse_input(self):
        with open('input.txt', 'r') as file:
            self.corrupted = [tuple(map(int, line.strip().split(','))) for line in file]

    def find_shortest_path(self, corrupted_set):
        target = (self.max_x, self.max_y)

        queue = deque([(0, 0, 0)])  # (x, y, steps)
        visited = set([(0, 0)])

        while queue:
            x, y, steps = queue.popleft()

            if (x, y) == target:
                return steps

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx <= self.max_x and 0 <= ny <= self.max_y and (nx, ny) not in corrupted_set and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

        return -1

    def part_one(self):
        corrupted_set = set()

        for i in range(1024):
            corrupted_set.add(self.corrupted[i])

        return self.find_shortest_path(corrupted_set)

    def part_two(self):
        corrupted_set = set(self.corrupted[:1024])

        for byte in self.corrupted[1024:]:
            corrupted_set.add(byte)
            if self.find_shortest_path(corrupted_set) < 0:
                return f"{byte[0]},{byte[1]}"

        return None 

if __name__ == '__main__':
    solution = Solution()
    print(f"Part One: {solution.part_one()}")
    print(f"Part Two: {solution.part_two()}")
