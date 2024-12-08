class Solution:

    def __init__(self):
        self.antennas = {}
        self.n_rows = 0
        self.n_cols = 0
        self.parse_input()

    def parse_input(self):
        
        with open("input.txt", 'r') as file:
           grid = [line.strip() for line in file]

        self.n_rows = len(grid)
        self.n_cols = len(grid[0])
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell.isalnum():  # antenna found
                    freq = cell
                    if freq not in self.antennas: #defaultdict?
                        self.antennas[freq] = []
                    self.antennas[freq].append((x, y))

    def calculate_antinodes(self, antenna1, antenna2):
        x1, y1 = antenna1
        x2, y2 = antenna2
        dx, dy = x2 - x1, y2 - y1
        return [(x2 + dx, y2 + dy), (x1 - dx, y1 - dy)]

    def part_one(self): 
        antinodes = set()
    
        for freq, positions in self.antennas.items():
            for i in range(len(positions)):
                for j in range(i+1, len(positions)):
                    new_antinodes = self.calculate_antinodes(positions[i], positions[j])
                    for antinode in new_antinodes:
                        x, y = antinode
                        if 0 <= x < self.n_rows and 0 <= y < self.n_cols:
                            antinodes.add(antinode)
        print(len(antinodes))
        return len(antinodes)
    
    def calculate_antinodes_lines(self, antenna1, antenna2):
        x1, y1 = antenna1
        x2, y2 = antenna2
        dx, dy = x2 - x1, y2 - y1

        antinodes = set([antenna1, antenna2])  # Include both antennas

        # Extend in positive direction
        x, y = x2, y2
        while 0 <= x < self.n_rows and 0 <= y < self.n_cols:
            antinodes.add((x, y))
            x += dx
            y += dy

        # Extend in negative direction
        x, y = x1, y1
        while 0 <= x < self.n_rows and 0 <= y < self.n_cols:
            antinodes.add((x, y))
            x -= dx
            y -= dy

        return list(antinodes)
        
        
    def part_two(self):
        antinodes = set()
    
        for freq, positions in self.antennas.items():
            for i in range(len(positions)):
                for j in range(i+1, len(positions)):
                    new_antinodes = self.calculate_antinodes_lines(positions[i], positions[j])
                    for antinode in new_antinodes:
                        x, y = antinode
                        if 0 <= x < self.n_rows and 0 <= y < self.n_cols:
                            antinodes.add(antinode)
        print(len(antinodes))
        return len(antinodes)
        
if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()