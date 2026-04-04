import sys
input = sys.stdin.readline

n = int(input())
tlist = [0]*n
plist = [0]*n
dp = [0]*(n+1)
for i in range(n):
    tlist[i],plist[i] = map(int,input().split())
    if tlist[i]+i <=n:
        dp[i+tlist[i]] = max(dp[i]+plist[i],dp[i+tlist[i]])
    else:
        dp[i + 1] = max(dp[i + 1], dp[i])

print((dp))
    