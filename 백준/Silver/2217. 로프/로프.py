import sys
n=int(sys.stdin.readline())
l=list(int(sys.stdin.readline()) for i in range(n))
l.sort()
q=[]
for i in range(n):
    q.append(l[i]*(n-i))
print(max(q))