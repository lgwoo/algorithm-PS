import sys
input = sys.stdin.readline

ans = 5

n = int(input())
for i in range(1,n):
    ans += (i+1)*3+1
print(ans%45678)
