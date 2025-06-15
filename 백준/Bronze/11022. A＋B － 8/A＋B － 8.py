i=int(input())
k=0
r=[]
for n in range(i):
    a=input().split()
    r=r+a
for m in range(i):
    k=k+1
    print("Case #%s:" %k, end=' ')
    print(r[2*m], "+",r[2*m+1],"=", end=' ')
    print(int(r[2*m])+int(r[2*m+1]))