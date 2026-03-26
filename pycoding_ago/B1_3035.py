import sys
input = sys.stdin.readline

r,c, zr, zc = map(int,input().split())
lis = []
for i in range(r):
    lis.append(input().strip())
for i in range(r):
    for k in range(zr):
        for j in range(c):
            print(lis[i][j]*zc,end="")
        print("")