n=int(input())
dp2=[0]*31
dp2[2]=3
for j in range(3,31):
    if j%2==0:
        dp2[j]=2+sum(dp2[:j-2])*2+dp2[j-2]*3
print(dp2[n])