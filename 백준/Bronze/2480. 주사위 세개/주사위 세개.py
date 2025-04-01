a,b,c=map(int,input().split())
l=[a,b,c]
if a==b and b==c:
    print(10000+a*1000)
elif a!=b and a!=c and b!=c:
    print(max(l)*100)
else:
    l.sort()
    print(1000+l[1]*100)