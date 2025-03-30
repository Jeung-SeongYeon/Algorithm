import sys
import collections
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

n,p,q=map(int,input().split())
dict=collections.defaultdict(int)
dict[0]=1
def dp(n):
    if dict[n]!=0:
        return dict[n]
    dict[n]=dp(n//p)+dp(n//q)
    return dict[n]
print(dp(n))