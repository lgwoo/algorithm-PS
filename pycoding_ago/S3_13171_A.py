import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
binb = bin(b)[2:][::-1]
c = 1
modd = 10 ** 9 + 7

for i in range(len(binb)):
    if binb[i] == '1':
        c = (c * (a % modd)) % (modd)
    a = (a * a) % (modd)    
print(c)