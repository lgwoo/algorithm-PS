import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
lis = list(map(int,input().split())) # 노래가락
m = int(input())
real = list(map(int,input().split())) # 꿈속 긴 노래
ans = []
indxlist = list(filter(lambda x: real[x] == lis[0],range(m))) # 시작 부분 인덱스 리스트
  
def dream(start,step,dept): # step 은 몇번 띄워져 있는지, dept는 노래가락의 몇번째 인지
    if dept == n:
        ans.append(step)
        return
    if start+step>=len(real):
        return
    if lis[dept] == real[start+step]:
        dream(start+step,step,dept+1)
    if dept == 1:
        dream(start,step+1,dept)
    
for i in indxlist:
    dream(i,1,1)
if ans:
    print(min(ans)-1,max(ans)-1)
else:
    print(-1)
