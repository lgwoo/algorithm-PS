import sys
input = sys.stdin.readline

n = int(input())
step = 0
while n>=10:
    n =  sum(map(int,str(n)))
    step += 1
print(step)
if n%3 != 0:
    print("NO")
else:
    print("YES")