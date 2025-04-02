m=int(input())
for j in range(m):
    n=int(input())
    l=[]
    i=0
    while n>=1:
        if n%2==1:
            l.append(i)
            i=i+1
            n=n//2
        else:
            i=i+1
            n=n//2
    print(" ".join(map(str,l)))
        