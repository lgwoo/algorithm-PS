import sys
from collections import deque
input = sys.stdin.readline
que = deque()
m,n = map(int,input().split())
tomato = []
visited = []
startpoint = []
dx = [0,1,0,-1] # 움직이는 위치
dy = [1,0,-1,0]
for i in range(n):
    temp = list(map(int,input().split()))
    tomato.append(temp)

    for k in range(m): # 번호가 1인칸을 찾아서 시작지점 정하기.
        if temp[k] == 1:
            startpoint.append((k,i))
    
def bfs():
    while que:
        s,que.popleft()



ans = 0
def findans():
    global ans
    for i in range(n):
        for k in range(m):
            if tomato[i][k]==0:
                ans = 0
                return
            else:
                ans = max(ans,tomato[i][k])
findans()
print(ans-1)