import sys

input = sys.stdin.readline

N = int(input())
graph = {}
for i in range(N):
    graph_info = list(map(int, input().split()))
    for node in range(len(graph_info)):
        node_num = node + 1
        # print(node_num)
        if graph_info[node] == 1:
            if (i+1) in graph:
                graph[i+1].append(node_num)
            else:
                graph[i+1] = [node_num]

# print(graph)
def dfs(graph, start, end):
    visit = [start]
    view = []
    
    while visit:
        point = visit.pop()
        if point == end:
            if len(view) == 0:
                pass
            else:
                return 1
        
        if point not in view:
            view.append(point)
            if point in graph:
                if start in graph[point]:
                    visit += list(set(graph[point]) - set(view))
                    visit.append(start)
                else:
                    visit += list(set(graph[point]) - set(view))
    return 0

path_matrix = [[0]*N for n in range(N)]
for i in range(N):
    for j in range(N):
        path_matrix[i][j] = dfs(graph, i+1, j+1)

for i in range(N):
    for j in range(N):
        print(path_matrix[i][j], end=' ')
    print('')