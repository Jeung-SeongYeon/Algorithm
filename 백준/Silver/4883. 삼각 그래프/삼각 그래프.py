cnt=1
while 1:
    n=int(input())
    if n==0:
        break
    l=[list(map(int, input().split())) for i in range(n)]
    dp=[[0,0,0] for i in range(n)]
    dp[0][0]=l[0][0]
    dp[0][1]=l[0][1]
    dp[0][2]=l[0][1]+l[0][2]
    dp[1][0]=dp[0][1]+l[1][0]
    dp[1][1]=min(dp[1][0],dp[0][1],dp[0][2])+l[1][1]
    dp[1][2]=min(dp[0][1],dp[0][2],dp[1][1])+l[1][2]
    for i in range(2,n):
        for j in range(3):
            if j==0:
                dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+l[i][j]
            if j==1:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])+l[i][j]
            if j==2:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+l[i][j]
    print(cnt,end='')
    print(".",dp[n-1][1])
    cnt+=1