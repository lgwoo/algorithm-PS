import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
tanfurit = list(map(int,(input().split())))

right = 0
left = 0
kind = defaultdict(int)
ans = 0
while right < n:
    kind[tanfurit[right]] +=1

    while len(kind)>2:
        kind[tanfurit[left]]-=1
        if kind[tanfurit[left]] == 0:
            del kind[tanfurit[left]]
        left +=1
    ans = max(ans,right-left+1)
    right+=1
print(ans)