import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
p,s = map(int,input().split())
print(n*p//100,end=' ')
ss = 0
for i in range(n):
    if lis[i] >=s:
        ss+=1
print(ss)