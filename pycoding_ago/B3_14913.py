import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
k=(c-a)/b
if int(k)==k and k>=0:
    print(int(k)+1)
else:
    print("X")