import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def kaing(M,N,x,y):
    if M>N:
        i = x
        plus = M
    else:
        i= y
        plus = N
    while(i<=lcm(M,N)):
        if((i-x)%M == 0 and (i-y)%N==0):
            return i
        else:
            i+=plus
    return -1


T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    print(kaing(M,N,x,y))



