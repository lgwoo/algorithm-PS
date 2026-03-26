import sys
input = sys.stdin.readline

n,m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
combination = []
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append((i,j))
        elif city[i][j]==2:
            chicken.append((i,j))
finalanswer = float('inf')

#gpt가 짜준 조합 구하는 코드
def comb(idx, path):
    global finalanswer
    if len(path) == m:
            sumdist = 0
            for housex,housey in house: # 여러 집들중 하나의 집의 최솟값 구하기
                dist = float('inf')
                for combix,combiy in path:
                    dist = min(dist,abs(housex-combix)+abs(housey-combiy))
                sumdist += dist
            finalanswer = min(finalanswer, sumdist)
            return

    for i in range(idx, len(chicken)):
        comb(i + 1, path + [chicken[i]])

comb(0, [])
print(finalanswer)