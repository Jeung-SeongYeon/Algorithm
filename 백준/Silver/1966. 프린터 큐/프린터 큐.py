n= int(input())
for i in range(n):
    m,k=map(int, input().split())
    l=list(map(int,input().split()))
    o=[]
    for j in range(m):
        o.append([j,l[j]])
    w=0
    while 1:
        if o[0][1]==max(l) and o[0][0]!=k:
            w+=1
            l.remove(max(l))
            o.pop(0)
        elif o[0][1]==max(l) and o[0][0]==k:
            w+=1
            break
        else:
            o.append(o[0])
            o.pop(0)
    print(w)