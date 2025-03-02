import sys
from collections import deque
input = sys.stdin.readline

n,m,h = map(int,input().split())
matrix = [[[] for i in range(m)] for _ in range(h)]

tomatocount = 0

for height in range(h):
    for i in range(m):
        row = list(map(int,input().split()))
        tomatocount += row.count(0)
        matrix[height][i] = row

move = [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]


que = deque()

def bfs():
    global tomatocount
    while que:
        x,y,zh = que.popleft()

        for i in range(6):
            dx,dy,dz = move[i]
            xx = x+dx; yy = y+dy; zz = zh+dz
            if 0<=xx<n and 0<=yy<m and 0<=zz<h:
                if matrix[zz][yy][xx] == 0:
                    matrix[zz][yy][xx] = matrix[zh][y][x]+1
                    tomatocount-=1
                    que.append((xx,yy,zz))


for i in range(h):
    for j in range(m):
        for k in range(n):
            if matrix[i][j][k] == 1:
                que.appendleft((k,j,i))
bfs()
if not tomatocount:
    ans = 0
    for i in range(h):
        for j in range(m):
            ans = max(ans,max(matrix[i][j]))
    print(ans-1)
else:
    print(-1)