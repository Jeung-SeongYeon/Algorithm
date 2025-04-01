import sys
n,m=map(int, sys.stdin.readline().split())
seq=list(int(sys.stdin.readline()) for i in range(n))
seq.sort()

def two_pointer(seq,n,m):
    start=0
    end=0
    cnt=float('inf')
    while start<n and end<n:
        if m<=seq[end]-seq[start]:
            cnt=min(cnt,seq[end]-seq[start])
            start+=1
        elif seq[end]-seq[start]<m:
            end+=1
    return cnt

print(two_pointer(seq,n,m))