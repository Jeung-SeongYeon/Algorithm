import sys
n=int(sys.stdin.readline())
m=list(map(int, sys.stdin.readline().split()))
dp=m.copy()
for i in range(1,n):
  cntlist=[]
  for j in range(i):
    if m[j]<m[i]:
      cntlist.append(dp[j])
  if cntlist==[]:
    pass
  else:
    dp[i]=max(cntlist)+m[i]
print(max(dp))