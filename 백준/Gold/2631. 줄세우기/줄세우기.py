import sys
n=int(sys.stdin.readline())
m=list(int(sys.stdin.readline()) for k in range(n))
dp=[1]*n
for i in range(1,n):
  cntlist=[]
  for j in range(i):
    if m[j]<m[i]:
      cntlist.append(dp[j])
  if cntlist==[]:
    pass
  else:
    dp[i]+=max(cntlist)
print(n-max(dp))