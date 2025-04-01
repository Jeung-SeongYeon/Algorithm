a,b = map(int,input().split())
c=int(input())
c1=c//60
c2=c%60
b1=b+c2
b2=b1//60
b3=b1%60
a1=a+c1+b2
a2=a1%24
print(a2,b3)