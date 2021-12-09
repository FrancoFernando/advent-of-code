import sys

def process_input():
    input = []
    with open("Advent/day9/input.txt", "r") as file:
        for line in file.readlines():
            input.append([int(x) for x in line.rstrip()])
    return input

def risk_level(input):
   
    rows = len(input)
    cols = len(input[0])

    risk = 0
    low_point_coord = []
    for i in range(rows):
        for j in range(cols):
            top = input[i - 1][j] if i > 0 else sys.maxsize
            bottom = input[i + 1][j]  if i + 1 < rows else sys.maxsize
            left = input[i][j - 1] if j > 0 else sys.maxsize
            right = input[i][j + 1] if j+1 < cols else sys.maxsize
            height = input[i][j]

            if height < left and height < right and height < top and height < bottom:
                risk += (height+1)
                low_point_coord.append([i,j])

    return [risk, low_point_coord]

def risk_level2(input, low_point_coord):

    offset = [(1,0), (-1,0), (0,1), (0,-1)]
    rows = len(input)
    cols = len(input[0])

    def is_outside(i, j, input):
        return not (0 <= i < len(input) and 0 <= j < len(input[0]))

    def dfs(input, i, j):
        if is_outside(i, j, input) or input[i][j] == 9 or (i, j) in visited:
            return 0

        visited.add((i, j))
        return 1 + sum(dfs(input,i+di, j+dj) for di, dj in offset)

    basins  = []
    visited = set()

    for i,j in low_point_coord:
            res.append(dfs(input,i, j))
    basins.sort()
    return basins [-1] * basins [-2] * basins [-3]