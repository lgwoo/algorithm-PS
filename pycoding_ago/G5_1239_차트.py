import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.sort()
comblist = set()
used = [False]*n
ans = 0
def comb(path:list, used:list): 
    '''
    재귀 함수를 이용하여 순열 구하기 
    '''
    global ans
    if len(path) == n: 
        comblist.add(tuple(path))
        ans = max(ans,sumlist(path))
        return
    for i in range(n):
        if used[i]==True:
            continue
        used[i] = True
        comb(path+[lis[i]],used)
        used[i] = False

def sumlist(li:list):
    ans = 0
    for i in range(1,n): # 1부터 시작하는 이유는 0부터 더해서 50이 나오는 경우에서 2번 카운트 되기 때문. (예: 40 10 25 25 은 40+10, 25+25이렇게 2번 카운트 됨)
        temp = 0
        for k in range(i,n):
            temp+=li[k]
            if temp == 50:
                ans +=1
            elif temp >50:
                break
    return ans
comb([],used)
print(ans)