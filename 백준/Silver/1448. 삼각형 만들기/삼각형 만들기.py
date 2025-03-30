import sys

input = sys.stdin.readline

N=int(input())
num_list=[]

for i in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort(reverse=True)

start_point = 0
while 1:
    if start_point > len(num_list)-3:
        print(-1)
        break
    a = num_list[start_point]
    b = num_list[start_point+1]
    c = num_list[start_point+2]
    if a < b + c:
        print(a+b+c)
        break
    else:
        start_point += 1