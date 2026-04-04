import sys
input = sys.stdin.readline

o = input().strip()
n = input().strip()

index = 0
togle = True
ans = 0
dp = [[[float('INF') for _ in range(2)] for _ in range(len(n))] for _ in range(len(o))]

for i in range(len(o)+1):
    for j in range(len(n)+1):
        # 1) 매칭 전이
        # if i < len(o) and j < len(n) and o[i] == n[j]:
        #     dp[i][j][togle] = min(dp[i][j][togle], dp[i-1][j-1][togle]+1)

        # 2) 삽입 전이
        # if j < len(n):
        #     ...


print(ans)

