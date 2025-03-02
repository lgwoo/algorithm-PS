import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split()))
lis.sort()

def dfs(dept:int,s:list):
    if dept == m:
        print(*s)
        return
    for loop in range(n):
        if lis[loop] not in s:
            ss = s.copy()
            ss.append(lis[loop])
            dfs(dept+1,ss)
    return
dfs(0,[])