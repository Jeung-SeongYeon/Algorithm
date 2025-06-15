n=int(input())
for i in range(n):
    l=list(map(int, input().split()))
    if l[0]==l[3] and l[1]==l[4] and l[2]==l[5]:
        print(-1)
    elif l[0]==l[3] and l[1]==l[4] and l[2]!=l[5]:
        print(0)
    else:
        if (l[0]-l[3])**2+(l[1]-l[4])**2==(l[2]+l[5])**2 or (l[0]-l[3])**2+(l[1]-l[4])**2==(l[2]-l[5])**2:
            print(1)
        elif (l[0]-l[3])**2+(l[1]-l[4])**2>(l[2]+l[5])**2 or (l[0]-l[3])**2+(l[1]-l[4])**2<(l[2]-l[5])**2:
            print(0)
        else:
            print(2)