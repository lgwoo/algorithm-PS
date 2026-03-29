import sys
input = sys.stdin.readline

n = int(input())
find = set([0])
lis = [0]*(n+1)
for i in range(1,n+1):
    k = lis[i-1] - i
    if 0 > k or k in find:
        lis[i] = lis[i-1]+i
        find.add(lis[i])
    else:
        lis[i] = k
        find.add(k) 
print(lis[n])