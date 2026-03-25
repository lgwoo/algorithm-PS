import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    lis=[]
    ans = 1
    a,b = map(int,input().split())
    while a:
        lis.append(a%b)
        a = a//b
    for i in range(len(lis)//2):
        if lis[i] != lis[len(lis)-1-i]:
            ans = 0
    print(ans)