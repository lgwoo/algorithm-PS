import sys
input = sys.stdin.readline
import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    lis = []
    anslis = []
    ans = 0
    for i in range(n):
        a,b = map(int,input().split())
        heapq.heappush(lis,(-a,b))
    a, b = heapq.heappop(lis)
    a = -a
    for i in range(1,n):
        c, d = heapq.heappop(lis)
        c = -c
        if b > d:
            pass
        else:
            heapq.heappush(anslis,(-b,a))
        a, b = c, d
    
    a, b = heapq.heappop(anslis)
    a = -a
    for i in range(len(anslis)):
        c, d = heapq.heappop(anslis)
        c = -c
        if b > d:
            pass
        else:
            ans +=1
        a, b = c, d
    print(ans)  