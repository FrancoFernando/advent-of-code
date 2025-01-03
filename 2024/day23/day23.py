from collections import defaultdict
import itertools

class Solution:
    def __init__(self):
        self.graph = defaultdict(set)
        self.computers = set()
        self.connections = set()
        self.parse_input()

    def parse_input(self):
        with open('input.txt', 'r') as file:
            for line in file:
                a, b = line.strip().split('-')
                self.graph[a].add(b)
                self.graph[b].add(a)
                self.computers.add(a)
                self.computers.add(b)
                self.connections.add((a, b))
                self.connections.add((b, a))

    def find_triangles(self):
        triangles = set()
        for a in self.graph:
            for b, c in itertools.combinations(self.graph[a], 2):
                if c in self.graph[b]:
                    triangle = tuple(sorted([a, b, c]))
                    triangles.add(triangle)
        return triangles

    def count_triangles_with_t(self, triangles):
        return sum(1 for triangle in triangles if any(computer.startswith('t') for computer in triangle))

    def part_one(self):
        triangles = self.find_triangles()
        t_count = self.count_triangles_with_t(triangles)       
        return t_count
    
    def find_largest_network(self):
        networks = [{c} for c in self.computers]
        for n in networks:
            for c in self.computers:
                if all(d in self.graph[c] for d in n):
                    n.add(c)
        return max(networks, key=len)
    
    def part_two(self):
        largest_network = self.find_largest_network()
        password = ",".join(sorted(largest_network))
        return password

if __name__ == '__main__':
    solution = Solution()
    print(solution.part_one())
    print(solution.part_two())