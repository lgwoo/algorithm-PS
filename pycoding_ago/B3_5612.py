import sys
input = sys.stdin.readline
n = int(input())
start = int(input())
ans = start
for i in range(n):
    a,b = map(int,input().split())
    if start + a-b < 0:
        print(0)
        exit()
    start = start+a-b
    ans = max(ans, start)
print(ans)