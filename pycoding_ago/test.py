tc = int(input())
for i in range(tc):
    n,m = map(int,input().split())
    if n<12 or m<4:
        print(-1)
    else:
        print(m*11+4)