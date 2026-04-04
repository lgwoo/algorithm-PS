import sys
input = sys.stdin.readline
h,x = map(int,input().split())
ans = 0
dx =1
nn = 1000000007
for i in range(1,h+1):
    dx *= x
    a = int(input())
    ans += (a*dx)%nn
print(ans%nn)