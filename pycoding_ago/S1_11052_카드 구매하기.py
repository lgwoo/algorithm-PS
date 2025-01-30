import sys
input = sys.stdin.readline
def max_card_price(N, prices):
    dp = [0] * (N + 1)
    
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i-j] + prices[j-1])
    
    return dp[N]

# 입력 받기
N = int(input())
prices = list(map(int, input().split()))

# 결과 출력
result = max_card_price(N, prices)
print(result)
