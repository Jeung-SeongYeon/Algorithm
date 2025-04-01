import sys
sys.setrecursionlimit(3000000)

input = sys.stdin.readline

H, W = map(int, input().split())
art = []

for i in range(H):
    tmp = list(map(int, input().split()))
    art.append(tmp)

maxi = 0
num = 0

def BFS(graph, start_x, start_y, H, W):
    global tmp_max
    if start_x < 0 or start_y < 0 or start_x >= H or start_y >= W:
        return
    
    if graph[start_x][start_y] == 0:
        return
    else:
        graph[start_x][start_y] = 0
        tmp_max += 1
        BFS(graph, start_x + 1, start_y, H, W)
        BFS(graph, start_x, start_y + 1, H, W)
        BFS(graph, start_x - 1 , start_y, H, W)
        BFS(graph, start_x, start_y - 1, H, W)

for i in range(H):
    for j in range(W):
        if art[i][j] == 1:
            tmp_max = 0
            num += 1
            BFS(art, i, j, H, W)
            if tmp_max > maxi:
                maxi = tmp_max

print(num)
print(maxi)