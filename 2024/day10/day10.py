from collections import deque

class Solution:

    def __init__(self):
        self.map = []
        self.trailheads = []
        self.parse_input()

    def parse_input(self):
        with open('test.txt', 'r') as file:
            self.map = [[int(x) for x in line.strip()] for line in file]
        self.trailheads = [(i, j) for i, row in enumerate(self.map) for j, height in enumerate(row) if height == 0]

    def count_trails(self, start):
        rows, cols = len(self.map), len(self.map[0])
        visited = set()
        queue = deque() 
        queue.append(start)
        peaks = set() #each peak must be counted once

        while queue:
            x, y = queue.popleft()
            
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if self.map[x][y] == 9:
                peaks.add((x, y))
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if self.map[nx][ny] == self.map[x][y] + 1:
                        queue.append((nx, ny))

        return len(peaks)

    def part_one(self):
        return sum(self.count_trails(trailhead) for trailhead in self.trailheads)
    
    def count_distinct_trails(self, start):
        rows, cols = len(self.map), len(self.map[0])
        queue = deque() 
        queue.append(start)
        distinct_trails = 0

        while queue:
            (x, y) = queue.popleft()

            if self.map[x][y] == 9:
                distinct_trails += 1
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if self.map[nx][ny] == self.map[x][y] + 1:
                        queue.append((nx, ny))

        return distinct_trails

    def part_two(self):  
        return sum(self.count_distinct_trails(trailhead) for trailhead in self.trailheads)


if __name__ == '__main__':
    day1 = Solution() 
    print(day1.part_one())
    print(day1.part_two())