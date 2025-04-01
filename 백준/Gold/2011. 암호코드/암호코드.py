data=list(map(int,input().strip()))
def crypto(x):
    if data==[] or data[0]==0:
        return 0
    n=len(data)
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        if 10<=data[i-2]*10+data[i-1]<=26:
            if data[i-1]==0:
                dp[i]=dp[i-2]
            else:
                dp[i]=dp[i-2]+dp[i-1]
        else:
            if data[i-1]==0:
                return 0
            else:
                dp[i]=dp[i-1]
    return dp[n]%1000000
print(crypto(data))