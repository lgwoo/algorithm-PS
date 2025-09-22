import sys
input = sys.stdin.readline
n = int(input())
table = [[ 0 for _ in range(501)] for _ in range(501)]
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            table[j][k] = 1
ans = sum(map(sum,table))
print(ans)