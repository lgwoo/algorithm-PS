import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    s = input().strip()
    ans = 0
    for k in range(len(s)):
        if k % 2==0:
            att = int(s[k])*2
            if att>=10:
                att = att//10 + att%10
        else:
            att = int(s[k])
        ans += att
    if ans % 10 == 0:
        print("T")
    else:
        print("F")