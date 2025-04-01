import sys
n=int(sys.stdin.readline())
tri=[[int(sys.stdin.readline())]]
for i in range(1,n):
    tmp=list(map(int, sys.stdin.readline().split()))
    tri.append(tmp)
dp=tri[-1]

for j in range(n-2,-1,-1):
    for k in range(j+1):
        dp[k]=max(dp[k],dp[k+1])+tri[j][k]
print(dp[0])