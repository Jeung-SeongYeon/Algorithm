n=int(input())
m=list(map(int, input().split()))
m.sort()
print(int(m[0])*int(m[n-1]))