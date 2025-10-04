import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.sort()
print(lis[(n-1)//2])