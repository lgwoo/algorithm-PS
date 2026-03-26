import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
lis = list(map(int, input().split()))
start = n//(m+1)
end = n

def check(x):
    if lis[0]-x>0:
        return False
    for i in range(m-1):
        if lis[i] + x < lis[i+1] - x:
            return False
    if lis[m-1] + x < n:
        return False
    return True

while start < end:
    mid = (start+end)//2
    if check(mid):
        end = mid
    else:
        start = mid + 1
print(end)