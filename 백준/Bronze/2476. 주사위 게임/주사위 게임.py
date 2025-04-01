n=int(input())
x=0
for i in range(n):
    a,b,c=map(int, input().split())
    l=[a,b,c]
    if a==b and b==c:
        y=10000+a*1000
    elif a!=b and a!=c and b!=c:
        y=max(l)*100
    else:
        l.sort()
        y=1000+l[1]*100
    if y>x:
        x=y
    else:
        pass
print(x)