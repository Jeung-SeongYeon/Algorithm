import heapq
def bfs(graph,root,n,m):
    que=[root]
    while que:
        a=heapq.heappop(que)
        w,i,j=a[0],a[1],a[2]
        if i==(n-1) and j==(m-1):
            return w
        if i<0 or j<0 or i>=len(graph) or j>=len(graph[0]) or graph[i][j]=='0':
            continue
        else:
            graph[i][j]='0'
        heapq.heappush(que,(w+1,i+1,j))
        heapq.heappush(que,(w+1,i-1,j))
        heapq.heappush(que,(w+1,i,j+1))
        heapq.heappush(que,(w+1,i,j-1))
n,m=map(int, input().split())
graph=list(list(str(input())) for i in range(n))
print(bfs(graph,(1,0,0),n,m))