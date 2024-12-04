class Solution:

    def __init__(self):
        self.target = 'XMAS'
        self.matrix = []
        self.parse_input()

        self.directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-Left, Up, Up-Right
            (0, -1),           (0, 1),   # Left, Right
            (1, -1),  (1, 0),  (1, 1)    # Down-Left, Down, Down-Right
        ]
        
        self.patterns = [
            # M.S
            # .A.
            # M.S
            [(0, 0, 'A'), (-1, -1, 'M'), (1, -1, 'M'), (-1, 1, 'S'), (1, 1, 'S')],
            
            # M.M
            # .A.
            # S.S
            [(0, 0, 'A'), (-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
            
            # S.M
            # .A.
            # S.M
            [(0, 0, 'A'), (-1, 1, 'M'), (1, 1, 'M'), (-1, -1, 'S'), (1, -1, 'S')],
            
            # S.S
            # .A.
            # M.M
            [(0, 0, 'A'), (1, -1, 'M'), (1, 1, 'M'), (-1, -1, 'S'), (-1, 1, 'S')]
        ]

    def parse_input(self):

        with open('input.txt', 'r') as file:
            for line in file:
                self.matrix.append(line.strip())

    def out_of_bounds(self, row, col):
        return row < 0 or row >= len(self.matrix) or col < 0 or col >= len(self.matrix[0])

    def dfs(self, row, col, direction, index):
        
        if self.out_of_bounds(row, col) or self.matrix[row][col] != self.target[index]:
            return 0
        
        if index == len(self.target)-1:
            return 1
        
        new_row, new_col = row + direction[0], col + direction[1]
        return self.dfs(new_row, new_col, direction, index + 1)

    def part_one(self):
        
        result = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'X':
                    for dir in self.directions:
                        result += self.dfs(i,j,dir,0)

        print(result)
        return result
    
    def check_pattern(self, center_row, center_col, pattern):
        for dr, dc, char in pattern:
            r, c = center_row + dr, center_col + dc
            if self.out_of_bounds(r, c) or self.matrix[r][c] != char:
                return False
        return True

    def part_two(self):
        
        count = 0
        rows, cols = len(self.matrix), len(self.matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                 if self.matrix[i][j] == 'A':  # Only check patterns when we find an 'A'
                    for pattern in self.patterns:
                        if self.check_pattern(i, j, pattern):
                            count += 1
                            break  # Found one orientation, no need to check others
        print(count)
        return count


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()