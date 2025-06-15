import sys
n=int(sys.stdin.readline())
l=list(map(int, sys.stdin.readline().split()))
q=[0]*1001
q[1]=l[0]
for i in range(2,n+1):
    o=[l[i-1]]
    for j in range(1,(i+1)//2+1):
        o.append(q[i-j]+l[j-1])
    q[i]=max(o)
print(q[n])