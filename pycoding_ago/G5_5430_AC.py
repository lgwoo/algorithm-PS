import sys
from collections import deque
input = sys.stdin.readline

ts = int(input())
for _ in range(ts):
    p = input().strip()
    n = int(input())
    lis = deque(eval(input()))
    roll = 1
    errorflag = True
    for i in p:
        if i == "R":
            roll *= -1
        elif i =="D":
            if len(lis)==0:
                print("error")
                errorflag = False
                break
            else:
                if roll ==1:
                    lis.popleft()
                else:
                    lis.pop()
    if errorflag:
        if roll == -1:
            lis.reverse()
        print(f"[{','.join(map(str, lis))}]")