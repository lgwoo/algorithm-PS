import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
idx = 0
for i in range(n):
    temp = 0
    if a == b:
        ans = 1
        break
    for k in range(n-i):
        if temp < a[k]:
            temp = a[k]
            idx = k
    if a[n-i-1] != temp:
        a[idx] = a[n-i-1]
        a[n-i-1] = temp
print(ans)