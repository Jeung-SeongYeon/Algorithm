import heapq
import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
route=[]
q=[]
for i in range(m):
    start,end,price=map(int, sys.stdin.readline().split())
    route.append((price,start,end))

start,end=map(int,sys.stdin.readline().split())
for j in route:
    if j[1]==start:
        heapq.heappush(q,j)

def daik(q,start,end,route):
    visited=[start]
    while q:
        a=heapq.heappop(q)
        price,city_2=a[0],a[2]
        if city_2==end:
            print(price)
            return
        else:
            if city_2 not in visited:
                visited.append(city_2)
                for j in route:
                    if j[1]==city_2:
                        heapq.heappush(q,(j[0]+price,j[1],j[2]))
    return

daik(q,start,end,route)