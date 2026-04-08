import sys
import heapq
input = sys.stdin.readline
n = int(input())
lis = []

for i in range(n):
    heapq.heappush(lis,int(input()))
ans = 0
while len(lis) >= 2:
    a = heapq.heappop(lis)
    b = heapq.heappop(lis)
    ans += a+b
    heapq.heappush(lis, a+b)
print(ans)