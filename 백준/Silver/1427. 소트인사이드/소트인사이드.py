m=list(map(int, list(input())))
m.sort(reverse=True)
for i in range(len(m)):
    print(m[i], end='')