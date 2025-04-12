from collections import deque

def bfs(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    que = deque([(0, 0, 1)])
    maps[0][0] = 0
    while que:
        now = que.popleft()
        x, y, cnt = now[0], now[1], now[2]
        if x == len(maps[0]) -1 and y == len(maps) - 1:
            return cnt
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if X < 0 or X >= len(maps[0]) or Y < 0 or Y >= len(maps):
                continue
            elif maps[Y][X] == 0:
                continue
            else:
                next_visit = (X, Y, cnt+1)
                maps[Y][X] = 0
                que.append(next_visit)
    return -1

def solution(maps):
    answer = bfs(maps)
    return answer