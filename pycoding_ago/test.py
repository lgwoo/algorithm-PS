import sys
input = sys.stdin.readline

<<<<<<< HEAD
a = input().strip()
b = input().strip()
c = input().strip()

print(int(a)+int(b)-int(c))
print(int(a+b)-int(c))
=======
n = int(input())
for i in range(n):
    t = int(input())
    t = t%25
    if t <17:
        print("ONLINE")
    else:
        print("OFFLINE")
>>>>>>> 5c24f2daf471fb0b31b01af8ec812672b04b6398
