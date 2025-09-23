import sys
input = sys.stdin.readline
import math

a,b,c = map(int,input().split())
bb = math.ceil(math.log2(b))
cc = math.ceil(math.log2(c))

if bb == cc:
    b = b - 2**(bb-1)
    c = c - 2**(cc-1)
    
    while math.ceil((math.log2(b))) == math.ceil(math.log2(c)):
        up = math.ceil((math.log2(b)))
        b = b - 2**(up-1)
        c = c - 2**(up-1)
    bb = math.ceil(math.log2(b))
    cc = math.ceil(math.log2(c))
    print(int(max(bb,cc)))
else:
    ans = max(bb,cc)
    print(int(ans))