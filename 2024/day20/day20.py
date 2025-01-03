from itertools import combinations

class Solution:
    def __init__(self):
        self.grid = {}
        self.start = None
        self.end = None
        self.distances = {}
        self.parse_input()
        self.calculate_distances()

    def parse_input(self):
        with open('input.txt', 'r') as file:
            for row, line in enumerate(file):
                for col, char in enumerate(line.strip()):
                    if char != '#':
                        self.grid[(row, col)] = char
                    if char == 'S':
                        self.start = (row, col)
                    elif char == 'E':
                        self.end = (row, col)

    def calculate_distances(self):
        self.distances = {self.start: 0}
        to_visit = [self.start]

        for position in to_visit:
            row, col = position
            for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if neighbor in self.grid and neighbor not in self.distances:
                    self.distances[neighbor] = self.distances[position] + 1
                    to_visit.append(neighbor)

    def manhattan_distance(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    def count_cheats(self, max_cheat_distance, min_time_saved):
        end_distance = self.distances[self.end]
        cheat_count = 0
        for (pos1, dist1), (pos2, dist2) in combinations(self.distances.items(), 2):
            cheat_distance = self.manhattan_distance(pos1, pos2)
            if cheat_distance <= max_cheat_distance:
                # Calculate time to end using this cheat
                time_to_end1 = dist1 + cheat_distance + (end_distance - dist2)
                time_to_end2 = dist2 + cheat_distance + (end_distance - dist1)
                time_saved = end_distance - min(time_to_end1, time_to_end2)
                if time_saved >= min_time_saved:
                    cheat_count += 1
        return cheat_count

    def part_one(self):
        return self.count_cheats(2, 100)

    def part_two(self):
        return self.count_cheats(20, 100)    

if __name__ == '__main__':
    solution = Solution()
    print(f"Part One: {solution.part_one()}")
    print(f"Part Two: {solution.part_two()}")
