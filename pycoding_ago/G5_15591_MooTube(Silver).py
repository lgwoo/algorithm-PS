import sys
sys.setrecursionlimit(10**4)
from collections import deque


input = sys.stdin.readline

N, Q = map(int,input().split())

graph = [[] for _ in range(N)]
for i in range(N-1):
    p,q,r = map(int,input().split())
    graph[p-1].append((q-1,r))
    graph[q-1].append((p-1,r))

def dfs(start,v):
    count = 0
    for nxt, weight in graph[start]:
        if visited[nxt] == 0 and weight >= v :
            visited[nxt] = 1
            count += 1
            count += dfs(nxt, v)
    return count

for i in range(Q):
    visited = [0]*N
    ans = 0
    a,b = map(int,input().split())
    visited[b-1] = 1
    print(dfs(b-1,a))
