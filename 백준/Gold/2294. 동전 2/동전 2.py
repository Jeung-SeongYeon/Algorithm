n,k=map(int, input().split())
val=list(set(int(input()) for i in range(n)))
dp=[-1]*(k+1)
dp[0]=0
for j in val:
    if j<=k:
        dp[j]=1
for i in range(1,k+1):
    price=set()
    for q in val:
        if i-q>=0:
            price.add(dp[i-q])
    price=price-{-1}
    if price:
        dp[i]=min(price)+1
if dp[k]==0:
    print(-1)
else:
    print(dp[k])