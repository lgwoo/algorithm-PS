import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
g = s.count("G")
h = s.count("H")
ss = s.count("S")
ss= ss//2

print(min(g,h,ss))