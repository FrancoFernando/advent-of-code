with open("2022/day1/input.txt", 'r') as file:

    calories_per_elf = []
    calories = 0
    
    for line in file:
        
        if line.strip():
            calories += int(line.strip())
        else:
            calories_per_elf.append(calories)
            calories = 0

    if calories != 0:
        calories_per_elf.append(calories)

    result = max(calories_per_elf)
    print(result)

    result = sum(sorted(calories_per_elf, reverse=True)[:3])
    print(result)
            
