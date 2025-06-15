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
    elif s=='back\n':
        if len(l)==0:
            print(-1)
        else:
            print(l[-1])
    elif s=='pop_front\n':
        if len(l)==0:
            print(-1)
        else:
            print(l.pop(0))
    elif s=='pop_back\n':
        if len(l)==0:
            print(-1)
        else:
            print(l.pop())
    elif s=='front\n':
        if len(l)==0:
            print(-1)
        else:
            print(l[0])
    else:
        if 'push_front' in s:
            k=int(s.lstrip('push_front '))
            l.insert(0,k)
        else:
            k=int(s.lstrip('push_back '))
            l.append(k)