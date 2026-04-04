import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.sort()
comblist = []
def comb(dept:int, mylist:list):
    if dept == n:
        comblist.append()
    for i in range(n):
        mylist.append(lis[i])