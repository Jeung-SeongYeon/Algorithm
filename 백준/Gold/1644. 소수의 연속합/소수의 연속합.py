import sys
from math import sqrt, floor
input=sys.stdin.readline

n = int(input())
data = [True for _ in range(n+1)]
data[0] = False
data[1] = False
ans = [0]

for i in range(2,int(sqrt(n))+1):
    if data[i] == True:
        for j in range(i+i , n+1, i):
            data[j] = False

for j in range(len(data)):
    if data[j]:
        ans.append(j+ans[-1])

def two_pointer(n,l):
    start=0
    end=0
    cnt=0
    while end<len(l):
        primes=l[end]-l[start]
        if primes==n:
            cnt+=1
            end+=1
        elif primes<n:
            end+=1
        elif primes>n:
            start+=1
    return cnt

print(two_pointer(n,ans))