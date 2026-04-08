import sys
from collections import deque
input = sys.stdin.readline
que = deque()
m,n,h = map(int,input().split())
tomato = [[]for i in range(n)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
startpoint = []
dx = [0,1,0,-1,0,0] # 움직이는 위치
dy = [1,0,-1,0,0,0]
dx = [0,0,0,0,1,-1]
for zz in range(h):
    for i in range(n):
        temp = list(map(int,input().split()))
        tomato[zz].append(temp)

        for k in range(m): # 번호가 1인칸을 찾아서 시작지점 정하기.
            if temp[k] == 1:
                que.append((1,k,i,zz))
                #startpoint.append((k,i))
                visited[zz][i][k] = True

            if temp[k] == -1: # 번호가 -1인 칸은 이미 방문한것으로 표시
                visited[zz][i][k] = True


#for i in startpoint:
 #   que.append((1,i[0],i[1]))
s = 0
while que:
    s,x,y,z = que.popleft()
    tomato[z][y][x] = s
    for i in range(6):
        nx,ny,nz = x+dx[i], y+dy[i],z+dx[i]
        if 0<= nx <m and 0<= ny <n and 0<=nz<h:
            if visited[nz][ny][nx] == False:
                que.append((s+1,nx,ny,nz))
                visited[nz][ny][nx] = True


ans = s
def findans():
    global ans
    for z in range(h):
        for i in range(n):
            for k in range(m):
                if visited[z][i][k] == False:
                    ans = 0
                    return

findans()
print(ans-1)