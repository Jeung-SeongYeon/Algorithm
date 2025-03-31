import sys
n=int(sys.stdin.readline())
l1=list(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
l2=list(map(int, sys.stdin.readline().split()))
def binary(a,l):
    s=0
    e=len(l)-1
    while s<=e:
        mid=(s+e)//2
        if a==l[mid]:
            return 1
        elif a<l[mid]:
            e=mid-1
        else:
            s=mid+1
    return 0
l1.sort()
for i in l2:
    print(binary(i,l1))