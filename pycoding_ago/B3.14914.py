import sys
import math
input = sys.stdin.readline
a,b = map(int,input().split())
c = math.gcd(a,b)
for i in range(1,c+1):  
    if c % i == 0:
        print(i,a//i,b//i)