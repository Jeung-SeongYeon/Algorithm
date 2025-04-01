n,k=map(int, input().split())
val=[int(input()) for i in range(n)]
dp=[0]*(k+1)
for j in val:
  if j<=k:
    dp[j]+=1
  for i in range(j+1,k+1):
    if i-j>=0:
      dp[i]+=dp[i-j]
print(dp[k])