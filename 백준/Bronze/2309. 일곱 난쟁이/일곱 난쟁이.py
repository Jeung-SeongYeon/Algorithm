from itertools import combinations
l=list(int(input()) for i in range(9))
c=list(combinations(l,7))
for j in range(len(c)):
    if sum(c[j])==100:
        m=list(map(int, c[j]))
        break
    else:
        pass
m.sort()
for k in m:
    print(k)