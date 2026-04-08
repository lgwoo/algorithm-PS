import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
tc = int(input())


def dfs(path):
    if visited[path] ==True:
        return
    visited[path] = True
    dfs(nlist[path]-1)
for i in range(tc):
    ans = 0
    n = int(input())
    nlist = list(map(int,input().split()))
    num = list(range(1,n+1))
    visited = [False]*n
    for j in range(n):
        if visited[j]==False:
            dfs(j)
            ans +=1
    print(ans)