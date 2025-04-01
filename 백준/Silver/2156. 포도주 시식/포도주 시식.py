import sys
n=int(sys.stdin.readline())
l=[int(sys.stdin.readline()) for i in range(n)]
k=[0]*10000
if n<3:
    print(sum(l))
else:
    k[0]=l[0]
    k[1]=l[0]+l[1]
    k[2]=max(l[0]+l[2],l[1]+l[2],k[1])
    for j in range(3,n):
        k[j]=max(k[j-1],k[j-2]+l[j],k[j-3]+l[j-1]+l[j])
    print(max(k))