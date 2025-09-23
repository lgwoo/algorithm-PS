import sys
input = sys.stdin.readline
n = int(input())
lis = []
classlist = [0]*10
std = [set() for _ in range(n)]
for i in range(n):
    lis.append(list(map(int,input().split())))
for i in range(5):
    for k in range(1,10):
        group = list(filter(lambda x : lis[x][i] == k, range(n)))
        if len(group) > 1:
            for j in group:
                std[j].update(group)
maxans = 0
anss = 0
for i in range(n):
    ans = len(std[i])
    if ans > maxans:
        maxans = ans
        anss = i+1
if anss == 0:
    anss = 1
print(anss)
    