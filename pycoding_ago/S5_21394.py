import sys
input = sys.stdin.readline

n = int(input())
lis = [0,0,0,0,0,0,0,0,0]
for i in range(n):
    temp = list(map(int,input().split()))
    temp[8] += temp[5]
    temp[5] = 0
    for i in range(9):
        pass