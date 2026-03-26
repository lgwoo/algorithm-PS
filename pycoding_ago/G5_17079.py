import sys
input = sys.stdin.readline
n = int(input())
home = [list(map(int,input().split())) for _ in range(n)]
dp =[[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
dp[1][0][0]=1 # 초기에 설정된 파이프

for i in range(n):
    for j in range(n):

        if (i + 1)<n and home[j][i+1] == 0:
            dp[i+1][j][0] += dp[i][j][0]+dp[i][j][2]
        if (j + 1)<n and home[j+1][i] == 0:
            dp[i][j+1][1] += dp[i][j][1] + dp[i][j][2]
        if (j + 1)<n and (i + 1)<n and home[j+1][i] ==0 and home[j][i+1] == 0 and home[j+1][i+1] == 0:
            dp[i+1][j+1][2] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]
print(sum(dp[n-1][n-1]))