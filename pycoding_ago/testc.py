import sys
input = sys.stdin.readline

n, A = map(int,input().split())
for i in range(n):
    p,l,d = map(int,input().split())
    for k in range( max(0,l*d-p),min(l*d+p,p+A) ):