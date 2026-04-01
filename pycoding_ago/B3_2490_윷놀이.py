import sys
input = sys.stdin.readline
ans = ['D','C','B','A','E']

for i in range(3):
    lis = list(map(int,input().split()))
    print(ans[sum(lis)])