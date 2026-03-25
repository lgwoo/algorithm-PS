import sys
input = sys.stdin.readline

n , l, k = map(int,input().split())
sb , bb = 0, 0
for i in range(n):
    a,b = map(int,input().split())
    if bb < k:
        if b <= l:
            bb+=1
            if sb + bb > k:
                sb -= 1
        elif a <= l:
            if sb + bb <k:
                sb +=1
print(sb*100+bb*140)
