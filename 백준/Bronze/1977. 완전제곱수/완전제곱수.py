import math
n=int(input())
m=int(input())
l=[]
add=0
for i in range(n,m+1):
    if math.sqrt(i)==math.floor(math.sqrt(i)):
        l.append(i)
        add=add+i
    else:
        pass
if len(l)==0:
    print(-1)
else:
    print(int(add))
    print(int(min(l)))