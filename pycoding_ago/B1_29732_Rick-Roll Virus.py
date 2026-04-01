import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
lis = [0]*n
string = input().strip()
for i in range(len(string)):
    if string[i] == "R":
        lis[max(0,i-k):min(n-1,i+k)+1] = [1] * ((min(n-1,i+k)+1)-max(0,i-k))

if sum(lis)<=m:
    print('Yes')
else:
    print('No')