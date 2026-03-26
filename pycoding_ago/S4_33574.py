import sys
from collections import deque

input = sys.stdin.readline

ans = deque()

t = int(input())
for _ in range(t):
    lis = list(map(int, input().split()))
    if lis[0] == 1:
        if lis[1] == 1:
            ans = deque(sorted(ans))
        else:
            ans = deque(sorted(ans, reverse=True))        
    else:
        ans.insert(lis[1], lis[2])
print(len(ans))
print(*ans)