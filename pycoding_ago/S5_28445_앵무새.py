import sys
input = sys.stdin.readline
lis = set()
a,b = input().split()
c,d = input().split()
lis.update([a,b,c,d])
lis = list(lis)
lis.sort()
for i in lis:
    for j in lis:
        print(i,j)