from math import lcm
import sys
n=int(input())
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    l=lcm(a,b)
    print(l)