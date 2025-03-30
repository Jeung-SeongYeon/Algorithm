import sys
n=int(sys.stdin.readline())
A=list(set(str(sys.stdin.readline()).rstrip('\n') for i in range(n)))
A1=sorted(A, key=lambda x:(len(x),x))
for j in range(len(A1)):
    print(A1[j])