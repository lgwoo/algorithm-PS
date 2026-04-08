import sys
from collections import deque
input = sys.stdin.readline
que = deque()
m,n = map(int,input().split())
tomato = []
visited = [[False for _ in range(m)] for _ in range(n)]
#startpoint = []
dx = [0,1,0,-1] # 움직이는 위치
dy = [1,0,-1,0]
for i in range(n):
    temp = list(map(int,input().split()))
    tomato.append(temp)

    for k in range(m): # 번호가 1인칸을 찾아서 시작지점 정하기.
        if temp[k] == 1:
            que.append((1,k,i))
            #startpoint.append((k,i))
            visited[i][k] = True

        if temp[k] == -1: # 번호가 -1인 칸은 이미 방문한것으로 표시
            visited[i][k] = True


#for i in startpoint:
 #   que.append((1,i[0],i[1]))
s = 0
while que:
    s,x,y = que.popleft()
    tomato[y][x] = s
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<= nx <m and 0<= ny <n:
            if visited[ny][nx] == False:
                que.append((s+1,nx,ny))
                visited[ny][nx] = True


ans = s
def findans():
    global ans
    for i in range(n):
        for k in range(m):
            if visited[i][k] == False:
                ans = 0
                return

findans()
print(ans-1)