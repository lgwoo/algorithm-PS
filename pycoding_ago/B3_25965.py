import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    answer = 0
    kk = int(input())
    lis = [0]*kk
    for j in range(kk):
        lis[j] = list(map(int,input().split()))
    k,d,a = map(int,input().split())
    for jj in range(kk):
        ans = lis[jj][0] * k + lis[jj][2]*a -lis[jj][1]*d
        if ans>0:
            answer += ans
    print(answer)