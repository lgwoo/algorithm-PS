from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
table = []
for i in range(n):
    table.append(list(map(int,input().split())))

ans = 0

def tet1(y,x):
    temp1 = 0
    temp2 = 0
    if x+3 <= m-1:
        for i in range(4):
            temp1 += table[y][x+i]
    if y+3 <= n-1:
        for i in range(4):
            temp2 += table[y+i][x]
    return max(temp1,temp2)

def tet2(y,x):
    temp1 = 0
    if x+1 <= m-1 and y+1 <= n-1:
        temp1 = table[y][x] +table[y+1][x] + table[y][x+1] + table[y+1][x+1]
    return temp1
def tet3(y,x):
    temp1 = 0
    temp2 = 0
    if x+1 <= m-1 and y+2 <= n-1:
        temp1 = table[y][x] + table[y+1][x] + table[y+2][x]
        temp1 += max(table[y][x+1],table[y+2][x+1])
        temp2 = table[y][x] + table[y][x+1] + table[y+1][x+1] + table[y+2][x+1]
    temp1 = max(temp1,temp2)
    temp2 = 0
    if x+2 <= m-1 and y+1 <= n-1:
        temp2 = table[y][x] + table[y][x+1] + table[y][x+2] + max(table[y+1][x],table[y+1][x+2])
        temp1 = max(temp1,temp2)
        temp2 = 0
        temp2 = table[y][x] + table[y+1][x] + table[y+1][x+1] + table[y+1][x+2]
    if x-2 >=0 and y+1 <=n-1:
        temp1 = max(temp1, table[y][x] + table[y+1][x] + table[y+1][x-1]+ table[y+1][x-2])
    if x-1 >=0 and y+2 <= n-1:
        temp2 = max(temp2, table[y][x]+table[y+1][x]+table[y+2][x]+table[y+2][x-1])
    return max(temp1,temp2)

def tet4(y,x):
    temp = 0
    if x+1<=m-1 and y+2<=n-1:
        temp = table[y][x] + table[y+1][x] + table[y+1][x+1] + table[y+2][x+1]
    if 0 <= x-1 and x+1 <= m-1 and y+1 <= n-1:
        temp = max(temp,table[y][x]+table[y+1][x]+table[y+1][x-1]+table[y][x+1])
    if 0 <= x-1 and y+2 <=n-1:
        temp = max(temp,table[y][x]+table[y+1][x]+table[y+1][x-1]+table[y+2][x-1])
    if x+2<=m-1 and y+1 <=n-1:
        temp = max(temp,table[y][x]+table[y][x+1]+table[y+1][x+1]+table[y+1][x+2])
    return temp

def tet5(y,x):
    temp = 0
    if x+2<=m-1 and y+1<=n-1:
        temp = table[y][x] + table[y][x+1] + table[y][x+2] + table[y+1][x+1]
    if x+1 <= m-1 and y+2 <= n-1:
        temp = max(temp,table[y][x]+table[y+1][x]+table[y+1][x+1]+table[y+2][x])
    if 0 <= x-1 and x+1 <= m-1 and y+1 <=n-1:
        temp = max(temp,table[y][x]+table[y+1][x]+table[y+1][x-1]+table[y+1][x+1])
    if 0<= x-1 and y+2 <=n-1:
        temp = max(temp,table[y][x]+table[y+1][x]+table[y+1][x-1]+table[y+2][x])
    return temp

a = 0
for i in range(n):
    for k in range(m):
        a = max(a,tet1(i,k),tet2(i,k),tet3(i,k),tet4(i,k),tet5(i,k))
print(a)
