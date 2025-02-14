'''
문제 정보
시간 제한	메모리 제한 제출	정답	맞힌 사람	정답 비율
1 초	128 MB  208147	94537	59968	43.215%

그래프 탐색 문제이다. bfs나 dfs를 사용하면 된다.

'''

import sys
from collections import deque
input = sys.stdin.readline

# 입력
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int,list(input().strip())))
    matrix.append(row)

# 필요변수 선연
move = [(0,1),(1,0),(-1,0),(0,-1)]


def bfs(start):
    que = deque()
    que.append(start)
    matrix[start[0]][start[1]] = 0
    counter = 0
    while que:
        xy = que.popleft()
        x = xy[0]
        y = xy[1]
        counter +=1
        for i in range(4):
            dx = x+move[i][0]
            dy = y+move[i][1]
            if 0<=dx<n and 0<=dy<n:
                if matrix[dx][dy] == 1:
                    que.append((dx,dy))
                    matrix[dx][dy] = 0 
    return counter
ans = []
for i in range(n):
    for k in range(n):
        if matrix[i][k] == 1:
            ans.append(bfs((i,k)))
print(len(ans))
ans.sort()
for i in ans:
    print(i)
        