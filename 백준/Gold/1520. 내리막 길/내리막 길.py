import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

row,col=map(int,input().split())
maze=list(list(map(int, input().split())) for i in range(row))
dp=list([-1]*col for i in range(row))
cnt=0

def dfs(maze,x,y):
    if x<0 or y<0 or x>=len(maze) or y>=len(maze[0]):
        return
    if x==len(maze)-1 and y==len(maze[0])-1:
        dp[x][y]=1
        return 1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    cnt=0
    for i in range(4):
        X=x+dx[i]
        Y=y+dy[i]
        if X<0 or Y<0 or X>=len(maze) or Y>=len(maze[0]) or maze[X][Y]>=maze[x][y]:
            continue
        if dp[X][Y]!=-1:
            cnt+=dp[X][Y]
            continue
        cnt+=dfs(maze,X,Y)
    dp[x][y]=cnt
    return dp[x][y]

print(dfs(maze,0,0))