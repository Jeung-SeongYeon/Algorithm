import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
mr=[]
for i in range(n):
    tmp=list(map(int, input().split()))
    mr.append(tmp)
mr.sort(key = lambda x:(x[1],x[0]))
meet=deque(mr)
cnt=0
b=0
for j in range(n):
    a=meet.popleft()
    if b<=a[0]:
        cnt+=1
        b=a[1]

print(cnt)