import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for i in range(N):
    tmp = list(input().replace("\n", "")) + ['0']
    grid.append(tmp)
grid.append(['0' for i in range(M+1)])

# print(grid)

maxVal = 0
for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
        if grid[i][j] == '1':
            if grid[i+1][j] != '0' and grid[i][j+1] != '0' and grid[i+1][j+1] != '0':
                grid[i][j] = str(int((math.sqrt(min(int(grid[i+1][j]), int(grid[i][j+1]), int(grid[i+1][j+1])))+1)**2))
            maxVal = max(maxVal, int(grid[i][j]))
print(maxVal)