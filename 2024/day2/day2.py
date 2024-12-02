class Solution:

    def __init__(self):
        self.reports = []
        self.parse_input()

    def parse_input(self):
        with open('input.txt', 'r') as file:
            for line in file:
                self.reports.append([int(num) for num in line.split()])

    def is_valid(self, report):
        if len(report) <= 1:
            return True
        
        is_ascending = all((report[i-1] < report[i] and report[i]-report[i-1] <= 3) for i in range(1, len(report)))
        is_descending = all((report[i-1] > report[i] and report[i-1]-report[i] <= 3) for i in range(1, len(report)))
        return is_ascending or is_descending

    def part_one(self):
        safe_reports = 0
        for report in self.reports:
            if self.is_valid(report):
                safe_reports += 1
        print(safe_reports)
        return safe_reports       

    def part_two(self):
        safe_reports = 0
        for report in self.reports:
            if self.is_valid(report):
                safe_reports += 1
            else:
                for i in range(len(report)):
                    if self.is_valid(report[:i] + report[i+1:]):
                        safe_reports += 1
                        break
        print(safe_reports)
        return safe_reports

if __name__ == '__main__':
    day1 = Solution() 
    day1.part_one()
    day1.part_two()