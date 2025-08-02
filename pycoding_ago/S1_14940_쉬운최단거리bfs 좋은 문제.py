import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
visitied = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 2:
            startp = (i,j)
        if row[j] == 0:
            visitied[i][j] = 0
    
movex = [0,1,-1,0]
movey = [1,0,0,-1]


def bfs(start):
    que = deque([start])
    visitied[start[0]][start[1]] = 0
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x+movex[i]
            ny = y+movey[i]
            if 0 <= nx < n and 0<= ny < m:
                if visitied[nx][ny] == -1:
                    visitied[nx][ny] = visitied[x][y]+1
                    que.append((nx,ny))

bfs(startp)

for i in visitied:
    print(*i)
