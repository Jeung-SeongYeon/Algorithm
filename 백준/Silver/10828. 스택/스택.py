import sys
l=[]
n=int(sys.stdin.readline())
for i in range(n):
    s=str(sys.stdin.readline())
    if s=='size\n':
        print(len(l))
    elif s=='empty\n':
        if len(l)==0:
            print(1)
        else:
            print(0)
    elif s=='top\n':
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
    elif s=='pop\n':
        if len(l)==0:
            print(-1)
        else:
            print(l.pop())
    else:
        k=int(s.lstrip('push '))
        l.append(k)