import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
c = 0
for i in s:
    if i !="C":
        c+=1

print(n//(c+1))