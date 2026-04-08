import sys
input = sys.stdin.readline
from collections import deque
que = deque()
n,m = map(int,input().split())
graph = [[ 0 for _ in range(n+1)] for _ in range(n+1)]

visited = [False]*(n+1)
for i in range(m):
    x,y,w = map(int,input().split())
    if w > graph[x][y]:
        graph[x][y] = w
        graph[y][x] = w 
start,end = map(int,input().split())

que.append((start,float('INF')))
while que:
    s,value = que.popleft()
    for i in range(1,n+1):
        if graph[s][i] != 0:
            if visited[i]==False :
                visited[i] = min(value,graph[s][i])
                que.append((i,visited[i]))
            elif visited[i] < min(value,graph[s][i]):
                visited[i] = min(value,graph[s][i])
                que.append((i,visited[i]))
print(visited[end])

