import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
line=[]
for i in range(n):
    line.append(list(map(int, input().split())))
line.sort(key = lambda x:(x[0],x[1]))
length=0
b=-float('inf')
lines=deque(line)
for j in range(n):
    a=lines.popleft()
    if b>a[0]:
        a[0]=b
    if a[1]<=a[0]:
        continue
    length+=a[1]-a[0]
    b=a[1]
    
print(length)