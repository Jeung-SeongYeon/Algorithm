import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
graph = [[0 for i in range(M)] for j in range(N)]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2):
        # print(j)
        for k in range(y1, y2):
            # print(k)
            graph[j][k] = 1

def BFS(graph, x, y, h, w, vistited = list):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if graph[x][y] == 1:
        return
    else:
        xs = [0, 0, 1, -1]
        ys = [1, -1, 0, 0]
        graph[x][y] = 1
        vistited.append((x, y))
        for i in range(4):
            BFS(graph, x + xs[i], y + ys[i], h, w, vistited)
        return

visitList = []
for i in range(N):
    for j in range(M):
        tmp = []
        BFS(graph, i, j, N, M, tmp)
        if tmp != []:
            visitList.append(len(tmp))

visitList.sort()
print(len(visitList))
if len(visitList) == 0:
        print(0)
else:
    for i in range(len(visitList)):
        print(visitList[i], end=" ")