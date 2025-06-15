import sys
n=int(sys.stdin.readline())
l=list(list(map(int,sys.stdin.readline().split())) for i in range(n))
l1=sorted(l,key=lambda x: (x[1],x[0]))
for j in range(n):
    print(l1[j][0],l1[j][1])