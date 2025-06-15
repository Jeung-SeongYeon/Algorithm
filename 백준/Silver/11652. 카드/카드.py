from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
dict=defaultdict(int)
for i in range(n):
    num=int(input())
    dict[num]+=1
a=sorted(dict.items(), key=lambda x: (-x[1],x[0]))
print(a[0][0])