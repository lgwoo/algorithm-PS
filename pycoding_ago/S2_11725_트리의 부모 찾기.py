import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
line = [[]for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    line[a].append(b)
    line[b].append(a)

ans = [0]*(n+1)

def dfs(nodeParent,node):
    for i in line[node]:
        if i != nodeParent:
            ans[i] = node
            dfs(node,i)

dfs(0,1)
for i in range(2,n+1):
    print(ans[i])