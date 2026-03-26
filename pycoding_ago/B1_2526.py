import sys
input = sys.stdin.readline
lis = []

n,p = map(int,input().split())
k = n
lis.append(k)
while True:
    k = k*n % p
    if k not in lis:
        lis.append(k)
    else:
        ans = lis.index(k)
        break
print(len(lis)-ans)
