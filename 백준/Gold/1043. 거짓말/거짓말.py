import sys

sys.setrecursionlimit(10000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

N, M = map(int, input().split())
info = list(map(int, input().split()))
truth_count = info[0]
truth_people = info[1:] if truth_count > 0 else []

parent = [i for i in range(N + 1)]

parties = []

for _ in range(M):
    party_info = list(map(int, input().split()))
    party_people = party_info[1:]
    parties.append(party_people)

    first_person = party_people[0]
    for person in party_people[1:]:
        union(first_person, person)

truth_roots = set(find(person) for person in truth_people)

answer = 0

for party in parties:
    if any(find(person) in truth_roots for person in party):
        continue
    else:
        answer += 1

print(answer)