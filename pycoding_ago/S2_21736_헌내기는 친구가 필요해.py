import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
matrix = []
startpoint = ()
for i in range(n):
    row = list(input().strip())
    matrix.append(row)
    for k in range(m):
        if row[k] == "X":
            visited[i][k] = True
        elif row[k] =="I":
            startpoint = (i,k)


movex = [0,1,-1,0]
movey = [1,0,0,-1]
ans = 0
def dfs(start):
    global ans
    visited[start[0]][start[1]] = True
    if matrix[start[0]][start[1]] == "P":
        ans +=1
    for i in range(4):
        if  0<=movex[i]+start[0]<n and 0<=movey[i]+start[1]<m:
            if visited[start[0]+movex[i]][start[1]+movey[i]] == False:
                dfs((start[0]+movex[i], start[1]+movey[i]))

dfs(startpoint)
if ans !=0:
    print(ans)
else:
    print("TT")