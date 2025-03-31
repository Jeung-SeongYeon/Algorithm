import re
n=str(input())
m=str(input())
text=re.sub(m,"",n)
print((len(n)-len(text))//len(m))