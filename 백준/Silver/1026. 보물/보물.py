import sys
n=int(sys.stdin.readline())
A=list(sys.stdin.readline().split())
B=list(sys.stdin.readline().split())
for j in range(n):
    A[j],B[j]=int(A[j]),int(B[j])
A.sort()
B1=sorted(B,reverse=True)
s=0
for i in range(n):
    s+=int(A[i])*int(B1[i])
print(s)