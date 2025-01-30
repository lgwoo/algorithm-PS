import sys
input = sys.stdin.readline

N,S = map(int,input().split())
arr = list(map(int,input().split()))
count = 0


def backtracking(sum:int, dept:int):
    if dept >= N:
        return
    
    global count
    sum += arr[dept]
    if sum==S:
        count+=1
    backtracking(sum,dept+1)
    backtracking(sum-arr[dept],dept+1)

backtracking(0,0)
print(count)