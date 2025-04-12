import sys
from collections import defaultdict

input = sys.stdin.readline

com_num = int(input())
net_num = int(input())

net_dict = defaultdict(list)

for i in range(net_num):
    computer, connect = map(int, input().split())
    net_dict[computer].append(connect)
    net_dict[connect].append(computer)

virus_list = []

def DFS(dict, q, start_com):
    if dict[start_com] is []:
        return
    else:
        for i in range(len(dict[start_com])):
            a = dict[start_com].pop()
            if a == 1:
                continue
            if a in q:
                continue
            q.append(a)
            DFS(dict, q, a)

DFS(net_dict, virus_list, 1)

print(len(virus_list))