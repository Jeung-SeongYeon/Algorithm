l=str(input())
l=l.upper()
s=list(set(l))
d={}
k=[]
for i in range(len(s)):
    a=l.count(s[i])
    k.append(a)
    d[a]=s[i]
if k.count(max(k))>1:
    print("?")
else:
    print(d[max(k)])