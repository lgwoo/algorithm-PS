import sys
from  collections import deque
input = sys.stdin.readline

lis = input().strip()
que = deque()
for i in lis:
    if i == '*':
        a = que.pop()
        b = que.pop()
        que.append((int(a) * int(b)))
    elif i == '+':
        a = que.pop()
        b = que.pop()
        que.append((int(a) + int(b)))
    elif i == '-':
        a = que.pop()
        b = que.pop()
        que.append((int(b) - int(a)))
    elif i == '/':
        a = que.pop()
        b = que.pop()
        que.append((int(b) // int(a)))
    else:
        que.append(i)
print(que[0])
    