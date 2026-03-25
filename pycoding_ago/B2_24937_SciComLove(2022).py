import sys
from collections import deque
queue = deque("SciComLove")
n = int(input())
n = n%10
for i in range(n):
    queue.append(queue.popleft())
print(*queue,sep='')