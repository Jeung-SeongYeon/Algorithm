import sys
input=sys.stdin.readline
n,m=map(int,input().split())
seq=[-1]+list(map(int,input().split()))
for i in range(1,n):
    seq[i+1]+=seq[i]

cnt=0
for j in seq:
    if j>=m:
        cnt=seq.index(j)
        break

def twopoint(seq,cnt):
    start=1
    end=cnt
    while start<=end and end<=n:
        if (seq[end]-seq[start-1])<m:
            end+=1
        elif (seq[end]-seq[start-1])>=m:
            cnt=min(cnt,(end-start)+1)
            start+=1
    return cnt

if cnt==0:
    print(cnt)
else:
    print(twopoint(seq,cnt))