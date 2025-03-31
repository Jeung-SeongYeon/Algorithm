import sys
sqrlist=[i**2 for i in range(1,318)]
n=int(sys.stdin.readline())
dp=list(range(n+1))
for i in range(2,n+1):
    l=[]
    for j in sqrlist:
        if j<=i:
            l.append(dp[i-j])
    dp[i]=min(l)+1
print(dp[n])