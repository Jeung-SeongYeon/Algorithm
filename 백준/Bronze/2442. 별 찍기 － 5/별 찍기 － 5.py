n=int(input())
l=list(2*i+1 for i in range(n))
for j in l:
    print(" "*((2*n-j)//2), end='')
    print("*"*j)