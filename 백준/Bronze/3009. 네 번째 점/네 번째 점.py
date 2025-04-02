l1=[]
l2=[]
for i in range(3):
    a,b=map(int,input().split())
    l1.append(a)
    l2.append(b)
l1.sort()
l2.sort()
z=l1[1]
x=l2[1]
for n in range(2):
    l1.remove(z)
    l2.remove(x)
print(l1[0],l2[0])