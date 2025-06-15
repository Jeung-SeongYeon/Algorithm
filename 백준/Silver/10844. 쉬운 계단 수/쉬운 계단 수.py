import sys
n=int(sys.stdin.readline())
dp=[[1]*10 for i in range(n+1)]
dp[1][0]=0
for j in range(2,n+1):
    for k in range(10):
        if k==0:
            dp[j][k]=dp[j-1][k+1]
        elif k==9:
            dp[j][k]=dp[j-1][k-1]
        else:
            dp[j][k]=dp[j-1][k-1]+dp[j-1][k+1]
print(sum(dp[n])%1000000000)