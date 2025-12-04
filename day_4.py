impt = """redacted uwu
"""

test = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

import numpy as np

txt = impt.splitlines()

plan = np.array([np.array(list(t)) for t in txt])
    
directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,1],[1,0],[1,-1]]

def count_neighbors(plan, i, j, directions):
    count = 0
    m, n = plan.shape
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n and plan[ni, nj] == '@':
            count += 1
    return count

def part_1():
    counter = 0
    m,n = plan.shape
    for i in range(m):
        for j in range(n):
            if plan[i][j]=="@":
                if count_neighbors(plan,i,j,directions) < 4: counter += 1
    return counter
    
def part_2():
    m,n = plan.shape
    removed = 0
    counter = 1
    while counter > 0:
        counter = 0
        for i in range(m):
            for j in range(n):
                if plan[i][j]=="@":
                    if plan[i][j]=="@":
                        if count_neighbors(plan,i,j,directions) < 4:
                            counter += 1
                            plan[i][j] = "x"
        removed += counter
                    
    return removed
    
print(part_2())

                    
            