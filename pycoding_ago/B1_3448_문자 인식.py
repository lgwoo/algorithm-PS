import sys

input = sys.stdin.readline
ans = []
n = int(input())
for i in range(n):
    ls = input().rstrip()
    r = 0
    a = 0
    while len(ls) != 0:
        r+= ls.count("#")
        a+= len(ls)
        ls = input().rstrip()
    print(f"Efficiency ratio is ",end='')
    a = (round((1-r/a)*1000)/10)
    if a.is_integer():
        print(f"{int(a)}%.")
    else:
        print(f"{a}%.")
