import sys
n=int(input())
for i in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b-c:
        print("does not matter")
    elif a<b-c:
        print("advertise")
    else:
        print("do not advertise")