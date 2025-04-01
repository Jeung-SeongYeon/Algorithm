n=int(input())
l=list(map(int, input().split()))
len1=1
len2=1
le1=1
le2=1
for i in range(n-1):
    if l[i]-l[i+1]>=0:
        le1+=1
    else:
        le1=1
    len1=max(len1,le1)

for i in range(n-1):
    if l[i]-l[i+1]<=0:
        le2+=1
    else:
        le2=1
    len2=max(len2,le2)
print(max(len1,len2))