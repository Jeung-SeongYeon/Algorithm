import sys
n,m=map(int, sys.stdin.readline().split())
seq=list(map(int, sys.stdin.readline().split()))

def two_pointer(seq,m):
    start=0
    end=0
    cnt=0
    while 1:
        if end>len(seq):
            break
        if sum(seq[start:end])<m:
            end+=1
        elif sum(seq[start:end])>m:
            start+=1
        elif sum(seq[start:end])==m:
            cnt+=1
            start+=1
    return cnt

print(two_pointer(seq,m))