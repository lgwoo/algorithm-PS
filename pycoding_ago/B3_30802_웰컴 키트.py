#import sys
#input = sys.stdin.readline

n = int(input())
size = list(map(int,input().split()))
tbundle,penbundle = map(int,input().split())
ansT = 0
for i in range(len(size)):
    ansT += (size[i]//tbundle) 
    if size[i] % tbundle != 0:
        ansT +=1
ansP = 0
ansp = n // penbundle
anspp = n % penbundle
print(ansT)
print(ansp,anspp)