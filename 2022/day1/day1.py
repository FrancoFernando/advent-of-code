def parse_input():
    with open("2022/day1/input.txt", 'r') as file:

        calories = [0]
        
        for line in file:
            
            if line.strip():
                calories[-1] += int(line.strip())
            else:
                calories.append(0)

    return calories

def part_one(calories):

    result = max(calories)
    print(result)

def part_two(calories):
    result = sum(sorted(calories, reverse=True)[:3])
    print(result)

if __name__ == '__main__':
    calories = parse_input()
    part_one(calories)
    part_two(calories)
            
