def prime(a):
    if a==1:
        return False
    elif a==2:
        return True
    else:
        for i in range(2,a):
            if a%i==0:
                return False
        return True
n=int(input())
m=list(input().split())
l=[]
for j in range(n):
    if prime(int(m[j]))==True:
        l.append(int(m[j]))
    else:
        pass
print(len(l))