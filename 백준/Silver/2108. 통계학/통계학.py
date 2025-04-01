import collections
import sys
n=int(sys.stdin.readline())
l=list(int(sys.stdin.readline()) for i in range(n))
l.sort()
print(round(sum(l)/n))
print(l[n//2])
j=collections.Counter(l).most_common()
if len(j)>1:
    if j[0][1]==j[1][1]:
        print(j[1][0])
    else:
        print(j[0][0])
else:
    print(j[0][0])
print(l[-1]-l[0])