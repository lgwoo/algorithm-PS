import sys
input = sys.stdin.readline

n = int(input())
lis = [0]*n
for i in range(n):
    lis[i] = i*2+1
print(*lis)