import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = sorted(list(map(int,input().split())))

ans = []
llll = []
visited = [False]*n
def dfs(deft,temp:list,visit:list):
    if deft == m:
        print(*temp)
        return
    
    for i in range(n):
        if visit[i] != True:
            visit[i] = True
            dfs(deft+1,temp + [lis[i]],visit[:])

dfs(0,llll,visited)
for i in ans:
    print(*i)