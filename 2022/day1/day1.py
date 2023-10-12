with open("2022/day1/input.txt", 'r') as file:

    calories = [0]
    
    for line in file:
        
        if line.strip():
            calories[-1] += int(line.strip())
        else:
            calories.append(0)

    result = max(calories)
    print(result)

    result = sum(sorted(calories, reverse=True)[:3])
    print(result)
            
