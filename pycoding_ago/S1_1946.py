import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    table = []
    for i in range(n):
        table.append(tuple(map(int,input().split())))
    table.sort(key=lambda x: (x[0],x[1])) #* x[0]이 같다면 x[1]로 정렬
    temp = table[0][1]
    ans = 0
    for i in range(1,n):
        if table[i][1] < temp:
            ans +=1
            temp = table[i][1]
    print(ans+1)