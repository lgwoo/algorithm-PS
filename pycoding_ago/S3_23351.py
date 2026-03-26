import sys
input = sys.stdin.readline

n,k,a,b = map(int,input().split())
lis = [k]*n
day = 0
startpoint = 0

while True:
    day += 1
    for i in range(startpoint,startpoint+a):
        lis[i] += b
    startpoint += a
    if startpoint >= n:
        startpoint = 0
    for i in range(n):
        lis[i]-=1
        if lis[i] == 0:
            print(day)
            exit(0)