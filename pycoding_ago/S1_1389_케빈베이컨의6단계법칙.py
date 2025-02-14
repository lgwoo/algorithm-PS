import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

connect = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    connect[a].append(b)
    connect[b].append(a)


def bfs(start):
    que = deque()
    que.append((start,0)) # 처음 들어오는 숫자에 단계(베이컨수)를 적어줌
    bakenNum = 0
    visited = [False]*(n+1) # 인덱스를 있는 그대로 쓰기 위해서 1개더 추가함

    visited[start]=True
    while que: 
        index = que.popleft() # index 예시 (1,0)
        bakenNum += index[1]
        for i in range(len(connect[index[0]])): # connect의 연결된 노드 수만큼 반복
            if visited[connect[index[0]][i]] == False:
                que.append((connect[index[0]][i],index[1]+1))
                visited[connect[index[0]][i]] = True
    return bakenNum

startbfs = bfs(1)
num = 1
for i in range(2,n+1):
    temp = bfs(i)
    if startbfs > temp:
        startbfs = temp
        num = i
print(num)


