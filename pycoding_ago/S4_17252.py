import sys
input = sys.stdin.readline

a = int(input())
lis = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
lis.sort(reverse=True)
ans = 0
for i in range(len(lis)):
    if a >= lis[i]:
        a = a-lis[i]
        if a == 0:
            ans = 1
if ans == 1:
    print("YES")
else:
    print("NO")
        