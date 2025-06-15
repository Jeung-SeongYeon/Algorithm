import sys
N=int(sys.stdin.readline())
seq=list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
dp=[[0]*N for j in range(N)]

for i in range(N):
    dp[i][i]=1

for i in range(N-1):
    if seq[i]==seq[i+1]:
        dp[i][i+1]=1

for j in range(N):
    for i in range(N):
        if j-i>=2:
            if seq[i]==seq[j] and dp[i+1][j-1]==1:
                dp[i][j]=1

for i in range(M):

    S,E=map(int, sys.stdin.readline().split())
    print(dp[S-1][E-1])