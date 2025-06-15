n=int(input())
for i in range(n):
    a,b=map(int, input().split())
    d=range(a,b+1)
    c=""
    for j in range(len(d)):
        c=c+str(d[j])
    c=" ".join(c)
    q=c.split()
    print(q.count('0'))