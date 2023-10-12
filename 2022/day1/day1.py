with open("2022/day1/input.txt", 'r') as file:

    items = []
    current_items = []
    
    for line in file:
        
        if line.strip():
            current_items.append(int(line.strip()))
        else:
            items.append(current_items)
            current_items = []

    if current_items:
        items.append(current_items)

    calories_per_elf = [sum(item) for item in items]
    result = max(calories_per_elf)
    print(result)

    result = sum(sorted(calories_per_elf, reverse=True)[:3])
    print(result)
            
