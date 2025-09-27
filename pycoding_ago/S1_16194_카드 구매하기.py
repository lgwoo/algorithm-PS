import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis = [0].append(lis)
dp = [0]*(n+1)
for i in range(n):
    dp[i] = lis[i]
    for k in range(1,i+1):
        dp[i] = min(dp[i],dp[i-k]+dp[k])
print(dp[n-1])