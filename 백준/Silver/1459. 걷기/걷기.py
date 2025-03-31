import sys
l=list(map(int, sys.stdin.readline().split()))
if l[2]>=l[3]:
    q=max(l[0],l[1])
    d=max(l[0],l[1])-min(l[0],l[1])
    if d%2==0:
        print(q*l[3])
    else:
        print((q-1)*l[3]+l[2])
elif 2*l[2]>l[3]>l[2]:
    z=min(l[0],l[1])
    c=max(l[0],l[1])-z
    print(z*l[3]+c*l[2])
else:
    print((l[0]+l[1])*l[2])