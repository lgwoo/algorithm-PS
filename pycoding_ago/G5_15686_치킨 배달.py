import sys
input = sys.stdin.readline
n,m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            house.append((i,j))
        elif city[i][j]==2:
            chicken.append((i,j))

#gpt가 짜준 조합 구하는 코드
def comb(idx, path):
    if len(path) == m:
        print(path)
        return

    for i in range(idx, len(chicken)):
        comb(i + 1, path + [chicken[i]])

comb(0, [])