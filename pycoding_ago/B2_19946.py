import sys
input = sys.stdin.readline
import math
a = 18446744073709551616
n = int(input())
print(64-int(math.log2(a-n)))
