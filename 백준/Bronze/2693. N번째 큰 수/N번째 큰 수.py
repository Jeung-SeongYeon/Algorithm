n=int(input())
for i in range(n):
    A=list(map(int, input().split()))
    A.sort(reverse=True)
    print(A[2])