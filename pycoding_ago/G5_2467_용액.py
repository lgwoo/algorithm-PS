import sys
input = sys.stdin.readline
n = int(input())
lis = map(int,input().split())

def divi(start, end, before):
    if start >=end:
        return start
    mid = (start+end)//2
    if before < abs(lis[mid]):
        end = mid
        before = abs(lis[mid])