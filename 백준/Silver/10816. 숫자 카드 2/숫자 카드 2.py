from collections import Counter 
import sys
n=int(sys.stdin.readline())
l=sorted(Counter(map(int, sys.stdin.readline().split())).items(), key= lambda x: x[0])
m=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))

def bin(l,a):
    m=[]
    for j in a:
        start=0
        end=len(l)-1
        while start<=end:
            mid=(start+end)//2
            if l[mid][0]==j:
                break
            elif l[mid][0]<j:
                start=mid+1
            else:
                end=mid-1
        if l[mid][0]==j:
            m.append(l[mid][1])
        else:
            m.append(0)
    print(' '.join(map(str,m)))

bin(l,a)