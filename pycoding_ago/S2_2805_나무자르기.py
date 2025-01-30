import sys
input = sys.stdin.readline

n,m = map(int,input().split())
trees = list(map(int,input().split()))

maxtree = max(trees)
start = 0

def cal(mid):
    ans = 0
    for i in trees:
        if i-mid>0:
            ans+=i-mid
    return ans

while start <= maxtree:
    mid = (start + maxtree)//2
    if m <= cal(mid):
        result = mid
        start = mid + 1
    else:
        maxtree = mid -1
    
print(result)