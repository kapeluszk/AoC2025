import numpy as np

with open("/home/kapelusz/PycharmProjects/AoC2025/day 7/input.txt") as f:
    lines = f.read().splitlines()

plan = np.array([np.array(list(l)) for l in lines ])

def part1(plan) -> int:
    rows, cols = plan.shape
    splitted = 0
    for r in range(rows):
        for c in range(cols):
            if plan[r, c] == 'S':
                plan[r+1,c] = '|'
            if plan[r,c] == '|':
                if r+1 < rows:
                    if plan[r+1,c] == '^':
                        if plan[r+1,c+1] != '|': plan[r+1,c+1] = '|'
                        if plan[r+1,c-1] != '|': plan[r+1,c-1] = '|'
                        splitted += 1
                    else:
                        plan[r+1,c] = '|'
    return splitted

def part2(plan) -> int:
    rows, cols = plan.shape
    paths_map = np.zeros((rows,cols))
    for r in range(rows):
        for c in range(cols):
            if plan[r, c] == 'S':
                paths_map[r+1,c] = 1
            if plan[r,c] == '|':
                if r+1 < rows:
                    if plan[r+1,c] == '^':
                        paths_map[r+1,c+1] += paths_map[r,c]
                        paths_map[r+1,c-1] += paths_map[r,c]
                    else:
                        paths_map[r+1,c] += paths_map[r,c]
    return int(np.sum(paths_map[rows-1,:]))


print(part1(plan))
print(part2(plan))
