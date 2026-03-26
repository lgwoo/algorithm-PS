import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    ans = 0
    cc = 0
    k = int(input())
    for e in range(k):
        a, b = input().split()
        cc += int(a)
        ans += int(a) * float(b)
    print(cc,ans/cc)
