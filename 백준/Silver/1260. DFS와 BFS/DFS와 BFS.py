import collections

def BFS(graph, start):
    visited=[]
    view=collections.deque([start])
    while view:
        n=view.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                next=list(set(graph[n])-set(visited))
                next.sort()
                view+=next
    return visited
    
def DFS(graph, start):
    visited=[]
    view=[start]
    while view:
        n=view.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                next=list(set(graph[n])-set(visited))
                next.sort(reverse=True)
                view+=next
    return visited

n,m,k=map(int,input().split())
graph={}
for i in range(m):
    n1,n2=map(int, input().split())
    if n1 not in graph:
        graph[n1]=[n2]
    else:
        graph[n1].append(n2)
    if n2 not in graph:
        graph[n2]=[n1]
    else:
        graph[n2].append(n1)
    
print(" ".join(str(i) for i in (DFS(graph,k))))
print(" ".join(str(i) for i in (BFS(graph,k))))