import sys
input = sys.stdin.readline

N = int(input())
dpList = [0, 1, 2]

for i in range(3, N+1):
    dpList.append((dpList[i-1]+dpList[i-2])%15746)
    
print(dpList[N])