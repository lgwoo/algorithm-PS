import sys
input = sys.stdin.readline

n = int(input())
tlist = [0]*n
plist = [0]*n
dp = [0]*n
for i in range(n):
    tlist[i],plist[i] = map(int,input().split())
    if tlist[i]+i =>n:
        continue
    dp[i+tlist[i]] = max(dp[i]+plist[i],dp[i+tlist[i]])
       
print(max(dp))
    