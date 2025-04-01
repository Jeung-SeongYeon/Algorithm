import sys
n=int(sys.stdin.readline())
ph=list(map(int, sys.stdin.readline().split()))

def binary(ph):
    start=0
    end=len(ph)-1
    cnt=abs(ph[start]+ph[end])
    result1=ph[start]
    result2=ph[end]
    while start<end:
        if ph[start]+ph[end]<0:
            if cnt>abs(ph[start]+ph[end]):
                cnt=abs(ph[start]+ph[end])
                result1=ph[start]
                result2=ph[end]
            start+=1
        elif ph[start]+ph[end]>0:
            if cnt>abs(ph[start]+ph[end]):
                cnt=abs(ph[start]+ph[end])
                result1=ph[start]
                result2=ph[end]
            end-=1
        elif ph[start]+ph[end]==0:
            result1=ph[start]
            result2=ph[end]
            break
    return result1, result2

a=binary(ph)
print(a[0],a[1])