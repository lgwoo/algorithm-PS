import sys
input = sys.stdin.readline
n,m = map(int,input().split())
anssum = 1
for i in range(n):
    ans = 0
    a,b = map(int,input().split())
    for k in range(b):
        ans += a*m**k
    anssum *= ans

base = ''
while anssum>0:
    anssum,mod = divmod(anssum,m)
    base += str(mod)
   
print(base[::-1])