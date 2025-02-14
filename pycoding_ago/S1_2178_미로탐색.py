import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
matrix = []

for i in range(n):
    row = list(map(int,list(input().strip())))
    matrix.append(row)

movex = [0,1,-1,0]
movey = [1,0,0,-1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        a,b = que.popleft()
        if a==n-1 and b==m-1:
            return matrix[n-1][m-1]
        for i in range(4):
            if 0 <= a+movex[i] < n and 0 <= b+movey[i]<m:
                if matrix[a+movex[i]][b+movey[i]] == 1:
                    matrix[a+movex[i]][b+movey[i]] = matrix[a][b]+1
                    que.append((a+movex[i],b+movey[i]))


a = bfs(0,0)
print(a)