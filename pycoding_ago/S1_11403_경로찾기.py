import sys
from collections import deque
matrix = []

n = int(input())
line = [[] for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    for k in range(n):
        if row[k]==1:
            line[i].append(k)



def bfs(start):
    visited = [0]*n
    que = deque()
    que.extend(start)
    while que:
        elem = que.popleft()
        visited[elem] = 1
        for i in line[elem]:
            if visited[i] == 0:
                que.append(i)
    return visited
        

for i in range(n):
    print(*bfs(line[i]))

