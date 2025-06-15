v=str(input())
v=" ".join(v)
l1=list(v.split())
l2=list(v.split())
l2.reverse()
if l1==l2:
    print(1)
else:
    print(0)