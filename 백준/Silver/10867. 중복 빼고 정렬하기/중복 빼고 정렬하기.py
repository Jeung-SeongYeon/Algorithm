n=int(input())
M=list(set(map(int,input().split())))
M.sort()
for i in range(len(M)-1):
    print(M[i],end=' ')
print(M[len(M)-1])