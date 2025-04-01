import heapq
import sys

n=int(sys.stdin.readline())
l=[]
for i in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        if l==[]:
            print(0)
        else:
            print(heapq.heappop(l))
    else:
        heapq.heappush(l,x)