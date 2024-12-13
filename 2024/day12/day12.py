from collections import defaultdict

class Solution:

    def __init__(self):
        self.grid = []
        self.parse_input()
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.grid_with_border = [['*'] * (self.cols + 2)]
        for row in self.grid:
            self.grid_with_border.append(['*'] + list(row) + ['*'])
        self.grid_with_border.append(['*'] * (self.cols + 2))

    def parse_input(self):

        with open('input.txt', 'r') as file:
            self.grid = [list(x.strip()) for x in file]
        

    def flood_fill(self, r, c, plant, visited):
        if r < 0 or r >= self.rows or c < 0 or c >= self.cols or visited[r][c] or self.grid[r][c] != plant:
            return 0, 0
        
        visited[r][c] = True
        area = 1
        perimeter = 0
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= self.rows or nc < 0 or nc >= self.cols or self.grid[nr][nc] != plant:
                perimeter += 1
            else:
                a, p = self.flood_fill(nr, nc, plant, visited)
                area += a
                perimeter += p
        
        return area, perimeter

    def part_one(self):
        total_price = 0
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if not visited[r][c]:
                    plant = self.grid[r][c]
                    area, perimeter = self.flood_fill(r, c, plant, visited)
                    total_price += area * perimeter

        return total_price
    
    def dfs(self, r, c, plant, visited):
        if r < 0 or r >= self.rows + 2 or c < 0 or c >= self.cols + 2 or visited[r][c] or self.grid_with_border[r][c] != plant:
            return 0, 0
        
        visited[r][c] = True
        area = 1
        sides = 0
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if self.grid_with_border[nr][nc] != plant:
                if (self.grid_with_border[nr + dc][nc + dr] == plant or 
                    self.grid_with_border[nr - dr + dc][nc - dc + dr] != plant):
                    sides += 1
            else:
                a, s = self.dfs(nr, nc, plant, visited)
                area += a
                sides += s
        
        return area, sides

    def part_two(self):
        total_price = 0
        visited = [[False for _ in range(self.cols + 2)] for _ in range(self.rows + 2)]
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                if not visited[r][c] and self.grid_with_border[r][c] != '*':
                    plant = self.grid_with_border[r][c]
                    area, sides = self.dfs(r, c, plant, visited)
                    price = area * sides
                    total_price += price

        return total_price

if __name__ == '__main__':
    day1 = Solution() 
    print(day1.part_one())
    print(day1.part_two())