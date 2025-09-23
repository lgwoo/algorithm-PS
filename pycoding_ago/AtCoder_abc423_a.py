import sys
input = sys.stdin.readline
x,c = map(int,input().split())

ans = x // (1000+c)
print(ans*1000)