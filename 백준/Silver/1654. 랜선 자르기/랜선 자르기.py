import sys
n,m=map(int, sys.stdin.readline().split())
l=[int(sys.stdin.readline()) for i in range(n)]
start=1
end=max(l)
b=[]
while start<=end:
    mid=(start+end)//2
    j=[q//mid for q in l]
    if sum(j)<m:
        end=mid-1
    else:
        start=mid+1
        b.append(mid)
print(max(b))