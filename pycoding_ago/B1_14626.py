import sys

input = sys.stdin.readline

weight = [1,3,1,3,1,3,1,3,1,3,1,3,1]
n = input().strip()

a = 0
b = 0
for i in range(13):
    if n[i] == '*':
        b = weight[i]
        continue
    a+=int(n[i])*weight[i]

if b == 1:
    print((10-a%10)%10)
else:
    for i in range(10):
        if (a+i*3)%10 == 0:
            print(i)
            break