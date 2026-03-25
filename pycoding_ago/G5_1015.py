import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = [0 for i in range(n)]

def findmax(lis:list)-> list:
    cnt = 0

    for _ in range(n):
        ma = min(a)
        if ma == 1001:
            return
        global ans
        for i in range(n):
            if a[i] == ma:
                ans[i] = cnt
                cnt += 1
                a[i] = 1001
findmax(a)
print(*ans)