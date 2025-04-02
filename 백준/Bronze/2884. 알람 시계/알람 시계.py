h,m=map(int, input().split())
h1=h*60
m1=m+h1
r=m1-45
print((r//60)%24,r%60)