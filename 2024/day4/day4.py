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

    def parse_input(self):

        with open('test.txt', 'r') as file:
            for line in file:
                self.matrix.append(line.strip())
        print(len(self.matrix),len(self.matrix[0]))

    def out_of_bounds(self, row, col):
        #print(row,col)
        return row < 0 or row >= len(self.matrix) or col < 0 or col >= len(self.matrix[0])

    def dfs(self, row, col, index):

        if index == len(self.target):
            return 1
        
        if self.out_of_bounds(row, col) or self.matrix[row][col] != self.target[index]:
            return 0
        
        if index == len(self.target)-1 and self.matrix[row][col] == self.target[index]:
            return 1
        
        intances = 0
        for (dx, dy) in self.directions:
            new_row, new_col = row + dx, col + dy
            intances += self.dfs(new_row, new_col, index + 1)

        return intances

    def part_one(self):
        
        result = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 'X':
                    result += self.dfs(i,j,0)

        print(result)
        return result

    def part_two(self):
        
        pass


if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()