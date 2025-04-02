import sys
sys.setrecursionlimit(100000000)
def maze(grid):
    def dfs(grid,i,j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
            return
        grid[i][j]=0
        
        dfs(grid,i+1,j)
        dfs(grid,i-1,j)
        dfs(grid,i,j+1)
        dfs(grid,i,j-1)
        dfs(grid,i+1,j+1)
        dfs(grid,i-1,j+1)
        dfs(grid,i+1,j-1)
        dfs(grid,i-1,j-1)
    cnt=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                dfs(grid,i,j)
                cnt+=1
    return cnt

while 1:
    col,row=map(int, input().split())
    if col==0 and row==0:
        break
    grid=list(list(map(int, input().split())) for k in range(row))
    print(maze(grid))