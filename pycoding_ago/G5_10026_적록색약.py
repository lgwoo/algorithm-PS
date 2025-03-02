# 좀더 최적화 할수있지만 귀찮...ㅎ

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
matrix = [[[]for _ in range(n)]for _ in range(n)]
visited = [[[True]for _ in range(n)]for _ in range(n)]
visitedRG = [[[True]for _ in range(n)]for _ in range(n)]


for i in range(n):
    matrix[i] = list(input().strip())

move = [(1,0),(0,1),(-1,0),(0,-1)]

que = deque()
# r g b = 0 1 2
def bfs(rgb):
    while que:
        x,y = que.popleft()
        for i in range(4):
            dx,dy = move[i]
            xx = x+dx; yy = y+dy
            if 0<=xx<n and 0<=yy<n:
                if visited[xx][yy] and matrix[xx][yy]==rgb:
                    visited[xx][yy] = False
                    que.append((xx,yy))
def bfsRG(rgb):
    while que:
        x,y = que.popleft()
        for i in range(4):
            dx,dy = move[i]
            xx = x+dx; yy = y+dy
            if 0<=xx<n and 0<=yy<n:
                if visitedRG[xx][yy] and matrix[xx][yy] in rgb:
                    visitedRG[xx][yy] = False
                    que.append((xx,yy))


num = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            que.append((i,j))
            num+=1
            if matrix[i][j] == "R":
                bfs("R")
            elif matrix[i][j] =="G":
                bfs("G")
            elif matrix[i][j] =="B":
                bfs("B")
numRG = 0
for i in range(n):
    for j in range(n):
        if visitedRG[i][j]:
            que.append((i,j))
            numRG+=1
            if matrix[i][j] in ["R","G"]:
                bfsRG(["R","G"])
            elif matrix[i][j] =="B":
                bfsRG("B")
        
        
print(num)
print(numRG)