import numpy as np

class Solution:

    def __init__(self):
        self.machines  = []
        self.parse_input()

    def parse_input(self):

        with open('input.txt', 'r') as file:
            content = file.read().strip()
            for machine in content.split('\n\n'):
                lines = machine.split('\n')
                ax, ay = map(int, lines[0].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
                bx, by = map(int, lines[1].split(': ')[1].replace('X+', '').replace('Y+', '').split(', '))
                px, py = map(int, lines[2].split(': ')[1].replace('X=', '').replace('Y=', '').split(', '))
                self.machines.append((ax, ay, bx, by, px, py))
        
    def solve_machine(self, ax, ay, bx, by, px, py, offset):
        tokens = 0
        
        px += offset
        py += offset
        a = round((py - ((by * px) / bx)) / (ay - ((by * ax) / bx)))
        b = round((px - ax * a) / bx)
        if ax * a + bx * b == px and ay * a + by * b == py:
            tokens += a * 3 + b

        return tokens

    def part_one(self):
        total_tokens = 0
        for machine in self.machines:
            tokens = self.solve_machine(*machine, 0)
            if tokens is not None:
                total_tokens += tokens
        return total_tokens

    def part_two(self):
        total_tokens = 0
        for machine in self.machines:
            tokens = self.solve_machine(*machine, 10000000000000)
            if tokens is not None:
                total_tokens += tokens
        return total_tokens

if __name__ == '__main__':
    day1 = Solution() 
    print(day1.part_one())
    print(day1.part_two())