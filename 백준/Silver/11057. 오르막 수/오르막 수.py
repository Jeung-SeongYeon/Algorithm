n=int(input())
dp=[[1,1,1,1,1,1,1,1,1,1] for i in range(n+1)]
for j in range(2,n+1):
    for k in range(1,10):
        dp[j][k]=sum(dp[j-1][:k+1])
print(sum(dp[n])%10007)