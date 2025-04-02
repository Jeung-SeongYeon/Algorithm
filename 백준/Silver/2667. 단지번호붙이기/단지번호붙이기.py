import sys
sys.setrecursionlimit(100000000)
def apart(grid,row):
    visited=[]
    l=[]
    def dfs(grid,i,j):
        if i<0 or i>=row or j<0 or j>=row or grid[i][j]!='1':
            return
        grid[i][j]='0'
        
        visited.append((i,j))
        
        dfs(grid,i+1,j)
        dfs(grid,i-1,j)
        dfs(grid,i,j+1)
        dfs(grid,i,j-1)
        
    cnt=0
    for i in range(row):
        for j in range(row):
            if grid[i][j]=='1':
                dfs(grid,i,j)
                l.append(len(visited))
                visited=[]
                cnt+=1
    l=sorted(l)
    print(cnt)
    for q in l:
        print(q)

row=int(input())
grid=list(list(map(str, input())) for k in range(row))
apart(grid,row)