n=int(input())
l1=list(i for i in range(1,n+1))
l2=sorted(l1, reverse=True)
l=l1+l2
l.remove(n)
for j in l:
    print(' '*(n-j),end='')
    print("*"*j)