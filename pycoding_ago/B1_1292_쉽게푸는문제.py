import sys
input = sys.stdin.readline

a,b = map(int,input().split())
lis = [0] * (b+1)
index = 1
def makelis():
    global index
    for i in range(b+1):
        for k in range(0,i):
            lis[index] = i
            index +=1
            if index>b:
                return
makelis()
print(sum(lis[a:b+1]))