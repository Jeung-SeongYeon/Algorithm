l0=[0]*41
l0[0]=1
l1=[0]*41
l1[1]=1
for i in range(2,41):
    l0[i],l1[i]=(l0[i-2]+l0[i-1]),(l1[i-2]+l1[i-1])
n=int(input())
for j in range(n):
    x=int(input())
    print(l0[x],l1[x])