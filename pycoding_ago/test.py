import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(depth, used, temp):
    if depth == m:
        print(*temp)
        return
    
    last = 0
    for i in range(n):
        if i not in used and last != nums[i]:
            used.add(i)
            dfs(depth + 1, used, temp + [nums[i]])
            used.remove(i)
            last = nums[i]

dfs(0, set(), [])