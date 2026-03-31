import sys
import math
input = sys.stdin.readline

n, p = map(int,input().split())
before = list(map(int,input().split()))
after = list(map(int,input().split()))
a = list(map(lambda x: x // math.gcd(*before), before))
b = list(map(lambda x: x // math.gcd(*after), after))

gab = 1
for i in range(n):
    if a[i]>b[i]:
        gab = max(gab,math.ceil(a[i]/b[i]))

print(sum(a), sum(b) *(gab))