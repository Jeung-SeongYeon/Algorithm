import sys
sys.setrecursionlimit(1000000000)
def cabbage(graph):
    def dfs(graph,i,j):
        if i<0 or i>=len(graph) or j<0 or j>=len(graph[0]) or graph[i][j]!=1:
            return

        graph[i][j]=0
        
        dfs(graph,i+1,j)
        dfs(graph,i-1,j)
        dfs(graph,i,j-1)
        dfs(graph,i,j+1)

    cnt=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]==1:
                dfs(graph,i,j)
                cnt+=1
    return cnt

Test=int(input())
for k in range(Test):
    col,row,cab=map(int, input().split())
    graph=[[0]*col for q in range(row)]
    for l in range(cab):
        j,i=map(int, input().split())
        graph[i][j]=1
    print(cabbage(graph))