class Solution:
    def __init__(self):
        self.registers = {'A': 0, 'B': 0, 'C': 0}
        self.program = []
        self.parse_input()

    def parse_input(self):
        with open('input.txt', 'r') as file:
            lines = file.readlines()
            self.registers['A'] = int(lines[0].split(': ')[1].strip())
            self.registers['B'] = int(lines[1].split(': ')[1].strip())
            self.registers['C'] = int(lines[2].split(': ')[1].strip())
            self.program = list(map(int, lines[4].split(': ')[1].strip().split(',')))

    def combo(self, a, b, c, value):
        if value < 4:
            return value
        if value == 4:
            return a
        if value == 5:
            return b
        if value == 6:
            return c
        return None

    def eval(self, a, b, c, ip):
        opcode = self.program[ip]
        arg = self.program[ip + 1]
        comb = self.combo(a, b, c, arg)
        
        if opcode == 0:
            return (None, a // (2 ** comb), b, c, ip + 2)
        elif opcode == 1:
            return (None, a, b ^ arg, c, ip + 2)
        elif opcode == 2:
            return (None, a, comb % 8, c, ip + 2)
        elif opcode == 3:
            return (None, a, b, c, ip + 2) if a == 0 else (None, a, b, c, arg)
        elif opcode == 4:
            return (None, a, b ^ c, c, ip + 2)
        elif opcode == 5:
            return (comb % 8, a, b, c, ip + 2)
        elif opcode == 6:
            return (None, a, a // (2 ** comb), c, ip + 2)
        elif opcode == 7:
            return (None, a, b, a // (2 ** comb), ip + 2)

    def run_program(self, a, b, c):
        ip = 0
        res = []
        while ip < len(self.program):
            out, a, b, c, ip = self.eval(a, b, c, ip)
            if out is not None:
                res.append(out)
            if ip >= len(self.program):
                break
        return res

    def find_self_replicating_input(self, index, partial_input):
        for candidate in range(8):
            a = partial_input * 8 + candidate
            output = self.run_program(a, 0, 0)
            if output == self.program:
                return a
            if output == self.program[index:]:
                ret = self.find_self_replicating_input(index - 1, a)
                if ret is not None:
                    return ret
        return None

    def part_one(self):
        result = self.run_program(self.registers['A'], self.registers['B'], self.registers['C'])
        return ','.join(map(str, result))

    def part_two(self):
        return self.find_self_replicating_input(len(self.program) - 1, 0)

if __name__ == '__main__':
    solution = Solution()
    print(f"Part One: {solution.part_one()}")
    print(f"Part Two: {solution.part_two()}")
