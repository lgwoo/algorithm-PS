import sys
import math
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
x = int(input())
ans = 0
a=0
for i in range(n):
    if math.gcd(s[i],x) == 1:
        ans += s[i]
        a +=1

print(ans/a)