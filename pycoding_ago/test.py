import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
<<<<<<< HEAD
s = list(map(int, input().split()))
if n %2 != 0:
    print("Bob")
else:
    print("Alice")   
=======
ans = 1
for i in range(n):
    ans += int(input())-1
print(ans)
>>>>>>> ac0e1a5f45660f697eea707f357edd9916089e35
