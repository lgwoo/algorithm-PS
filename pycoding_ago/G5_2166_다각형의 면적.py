import sys
input = sys.stdin.readline

n = int(input())
lis = []

for i in range(n):
    lis.append(tuple(map(int,input().split())))
lis.append(lis[0])
a = 0
b = 0
for i in range(n):
    a += lis[i][0]*lis[i+1][1]
    b += lis[i][1]*lis[i+1][0]
print(abs(a-b)*0.5)
