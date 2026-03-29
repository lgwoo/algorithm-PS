import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split()))
for i in range(m):
    qury = list(map(int,input().split()))
    if qury[0] == 1:
        print(sum(lis[qury[1]-1:qury[2]]))
        lis[qury[1]-1],lis[qury[2]-1] = lis[qury[2]-1],lis[qury[1]-1]
    else:
        ans = 0
        for k in range(n):
            if qury[1]-1 <= k <= qury[2]-1:
                ans+=lis[k]
            if qury[3]-1 <=k <=qury[4]-1:
                ans-=lis[k]
        print(ans)