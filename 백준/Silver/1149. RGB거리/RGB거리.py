n=int(input())
data=[]
for i in range(n):
  l=list(map(int, input().split()))
  data.append(l)
dp1=[0]*(n+1)
dp2=[0]*(n+1)
dp3=[0]*(n+1)
dp1[1]=data[0][0]
dp2[1]=data[0][1]
dp3[1]=data[0][2]
for j in range(2,n+1):
  dp1[j]=data[j-1][0]+min(dp2[j-1],dp3[j-1])
  dp2[j]=data[j-1][1]+min(dp1[j-1],dp3[j-1])
  dp3[j]=data[j-1][2]+min(dp2[j-1],dp1[j-1])
print(min(dp1[n],dp2[n],dp3[n]))