b=100
i=0
l=[]
while b:
    b=b-1
    i=i+1
    for j in range(i):
        l.append(i)
a,c=map(int, input().split())
s=sum(l[a-1:c])
print(s)