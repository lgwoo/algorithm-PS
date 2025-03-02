import sys
import heapq
input = sys.stdin.readline
que = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if que:
            ans = heapq.heappop(que)
            print(ans[1])
        else:
            print(0)
    else:
        heapq.heappush(que,(abs(x),x))
