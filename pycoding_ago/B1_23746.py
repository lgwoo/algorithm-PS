import sys
input = sys.stdin.readline
dic = {}
ans = ''
n = int(input())
for i in range(n):
    a,b = input().split()
    dic[b] = a
s = input().strip()
for i in s:
    ans = ans+dic[i]
a,b = map(int,input().split())
print(ans[a-1:b])