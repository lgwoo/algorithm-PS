import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())

startpoint = []
matrix = []
day = 0
movex = [0,1,-1,0]
movey = [1,0,0,-1]


for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] == 1:
            startpoint.append((i,j,0))

def bfs(start):
    global day
    que = deque(start)
    while que:
        x,y,s = que.popleft()
        day = s
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            for i in range(4):
                dx = x+movex[i]
                dy = y+movey[i]
                if 0<=dx<n and 0<=dy<m:
                    que.append((dx,dy,s+1))

for i in startpoint:
    matrix[i[0]][i[1]] = 0

bfs(startpoint)

has_zero = any(0 in row for row in matrix)

if(has_zero):
    print(-1)
else:
    print(day-1)