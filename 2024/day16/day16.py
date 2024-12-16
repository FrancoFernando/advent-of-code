import heapq
from collections import defaultdict, namedtuple

State = namedtuple('State', ['x', 'y', 'direction'])

class Solution:
    def __init__(self):
        self.maze = []
        self.parse_input()
        self.rows = len(self.maze)
        self.cols = len(self.maze[0])
        self.start = self.find_position('S')
        self.end = self.find_position('E')
        self.directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # Right, Up, Left, Down

    def parse_input(self):
        with open('input.txt', 'r') as file:
            self.maze = [list(line.strip()) for line in file]

    def find_position(self, char):
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == char:
                    self.maze[y][x] = '.'  # Replace S and E with .
                    return (y, x)
        return None

    def adjacent_states(self, state):
        x, y, d = state
        # Rotate
        yield 1000, State(x, y, (d-1)%4)
        yield 1000, State(x, y, (d+1)%4)
        # Move forward
        dx, dy = self.directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] != '#':
            yield 1, State(nx, ny, d)

    def part_one(self):
        start_state = State(self.start[0], self.start[1], 0)  # Start facing right
        pq = [(0, start_state)]
        distances = defaultdict(lambda: float('inf'))
        distances[start_state] = 0
        predecessors = defaultdict(set)

        while pq:
            dist, current = heapq.heappop(pq)
            if (current.x, current.y) == self.end:
                return dist, distances, predecessors

            for cost, next_state in self.adjacent_states(current):
                new_dist = dist + cost
                if new_dist < distances[next_state]:
                    distances[next_state] = new_dist
                    predecessors[next_state] = {current}
                    heapq.heappush(pq, (new_dist, next_state))
                elif new_dist == distances[next_state]:
                    predecessors[next_state].add(current)

        return float('inf'), distances, predecessors

    def part_two(self):
        best_dist, distances, predecessors = self.part_one()
        end_states = [state for state in distances if (state.x, state.y) == self.end and distances[state] == best_dist]
        
        # Backtrack to find all cells in optimal paths
        cells_in_best_paths = set()
        to_visit = set(end_states)
        
        while to_visit:
            current = to_visit.pop()
            cells_in_best_paths.add((current.x, current.y))
            to_visit.update(predecessors[current] - set(cells_in_best_paths))

        return len(cells_in_best_paths)

if __name__ == '__main__':
    solution = Solution()
    print(f"Part One: {solution.part_one()[0]}")
    print(f"Part Two: {solution.part_two()}")