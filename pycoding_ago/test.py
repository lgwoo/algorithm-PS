import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
if n %2 != 0:
    print("Bob")
else:
    print("Alice")   