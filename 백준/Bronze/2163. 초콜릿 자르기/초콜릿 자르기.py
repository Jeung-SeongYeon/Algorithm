a,b=map(int,input().split())
r1=(a-1)+a*(b-1)
r2=(b-1)+b*(a-1)
r=[r1,r2]
print(min(r))