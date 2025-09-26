import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    t = int(input())
    t = t%25
    if t <17:
        print("ONLINE")
    else:
        print("OFFLINE")