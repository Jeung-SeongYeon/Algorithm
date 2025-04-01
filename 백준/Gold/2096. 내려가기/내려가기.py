n=int(input())
max_dp=[[0,0,0] for _ in range(2)]
min_dp=[[0,0,0] for _ in range(2)]
score=list(map(int,input().split()))
min_dp[0]=score.copy()
max_dp[0]=score.copy()

for i in range(1,n):
    tmp=list(map(int,input().split()))
    t=i%2
    for j in range(3):
        if j==1:
            max_dp[t][j]=max(max_dp[t-1])+tmp[1]
            min_dp[t][j]=min(min_dp[t-1])+tmp[1]
        if j==0:
            max_dp[t][j]=max(max_dp[t-1][0],max_dp[t-1][1])+tmp[0]
            min_dp[t][j]=min(min_dp[t-1][0],min_dp[t-1][1])+tmp[0]
        if j==2:
            max_dp[t][j]=max(max_dp[t-1][1],max_dp[t-1][2])+tmp[2]
            min_dp[t][j]=min(min_dp[t-1][1],min_dp[t-1][2])+tmp[2]
            
print(max(max_dp[n%2-1]),min(min_dp[n%2-1]))