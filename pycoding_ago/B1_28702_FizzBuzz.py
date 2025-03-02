import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()
if a.isdigit():
    d = int(a)+3
elif b.isdigit():
    d = int(b)+2
else:
    d = int(c)+1

if d % 3 == 0 and d % 5 == 0:
    print("FizzBuzz")
elif d % 3 == 0 and d % 5 != 0:
    print("Fizz")
elif d % 3 != 0 and d % 5 == 0:
    print("Buzz")
else:
    print(d)