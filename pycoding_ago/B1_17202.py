import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()

c = "".join(x+y for x, y in zip(a, b))

for i in range(14):
    ans = ""
    for j in range(1,len(c)):
        ans += str((int(c[j]) + int(c[j-1])) % 10)
    c = ans
print(c)