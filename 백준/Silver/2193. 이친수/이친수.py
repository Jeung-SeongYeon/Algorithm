import sys
input = sys.stdin.readline

li = []
li.append(1)
li.append(1)
N = int(input())
if N < 3:
    print(1)
else:
    for i in range(2, N):
        tmp = li[i-1] + li[i-2]
        li.append(tmp)

    print(li[N-1])