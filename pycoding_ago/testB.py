import sys
input = sys.stdin.readline

n,m,x = map(int,input().split())
xsosu = []
for i in range(1,int(x**0.5)+1):
    if x%i ==0:
        xsosu.append((i,x//i))
ans = 0
for xx,yy in xsosu:
    if (xx<=n and yy<=m):
        ans = 1
        print(1)
        print(0,0,xx,yy)
        break
    elif (xx<=m and yy<=n):
        ans = 1
        print(1)
        print(0,0,yy,xx)
        break
if ans == 0:
    xx = x//n
    yy = x%n 
    print(2)
    print(0,0,n,xx)
    print(0,xx,yy,xx+1)
#    else:
#        yy = x//m
#        xx = x%m
#        print(2)
#        print(0,0,yy,m)
#        print(0,yy,xx,yy+1)