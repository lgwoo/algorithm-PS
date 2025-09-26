import sys
input = sys.stdin.readline

n = int(input())
lis = [0]*n
count = 0
def roopqueen(deft):
    global count
    if deft == n:
        count+=1
        return
    for i in range(n):
        lis[deft] = i
        if isQueen(deft):
            roopqueen(deft+1)



def isQueen(deft):
    for i in range(deft):
        if lis[i] == lis[deft]:
            return False
        elif abs(deft-i) == abs(lis[deft]-lis[i]):
            return False
    return True

roopqueen(0)
print(count)