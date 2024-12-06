from collections import defaultdict

class Solution:

    def __init__(self):
        self.map_grid = []
        self.rows = 0
        self.cols = 0
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.parse_input()

    def parse_input(self):
        
        with open("input.txt", 'r') as file:
           self.map_grid = [list(row.strip()) for row in file]
           self.rows = len(self.map_grid)
           self.cols = len(self.map_grid[0])
    
    def find_guard(self):
        
        guard_symbols = '^>v<'

        guard_pos = next((i, j) for i, row in enumerate(self.map_grid) 
                 for j, cell in enumerate(row) if cell in guard_symbols)
        
        guard_dir = guard_symbols.index(self.map_grid[guard_pos[0]][guard_pos[1]])

        return (guard_pos, guard_dir)
    
    def has_left(self, position):
    
        if not (0 <= position[0] < self.rows and 0 <= position[1] < self.cols):
            return True
        return False

    def part_one(self): 
         
        (guard_pos, guard_dir) = self.find_guard()
        visited = set([guard_pos])

        while True:
        
            next_pos = (guard_pos[0] + self.directions[guard_dir][0], 
                        guard_pos[1] + self.directions[guard_dir][1])
            
            if self.has_left(next_pos):
                break  
            
            # Check if there's an obstacle
            if self.map_grid[next_pos[0]][next_pos[1]] == '#':
                guard_dir = (guard_dir + 1) % 4  # Turn right
            else:
                guard_pos = next_pos
                visited.add(guard_pos)

        print(len(visited))
        return len(visited)
    
    def can_exit(self, start_pos, start_dir):
        guard_pos = start_pos
        guard_dir = start_dir
        visited = set()

        while True:
            # Unique state identifier
            state = (guard_pos, guard_dir)
            
            if state in visited:
                return True  # Guard is stuck in a loop
            
            visited.add(state)

            next_pos = (guard_pos[0] + self.directions[guard_dir][0], 
                        guard_pos[1] + self.directions[guard_dir][1])
            
            if self.has_left(next_pos):
                return False  
            
            # Check if there's an obstacle
            if self.map_grid[next_pos[0]][next_pos[1]] == '#':
                guard_dir = (guard_dir + 1) % 4  # Turn right
            else:
                guard_pos = next_pos
    
    def part_two(self):
        (guard_pos, guard_dir) = self.find_guard()
        obstacle_positions = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) != guard_pos and self.map_grid[i][j] == '.':
                    self.map_grid[i][j] = '#'
                    
                    if self.can_exit(guard_pos, guard_dir):
                        obstacle_positions += 1

                    self.map_grid[i][j] = '.'
                    
        print(obstacle_positions)
        return obstacle_positions
        
if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()