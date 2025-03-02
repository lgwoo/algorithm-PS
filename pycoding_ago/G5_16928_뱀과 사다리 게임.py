import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
uv = {}
matrix = [500]*101
matrix[1] = 0
for i in range(n+m):
    u,v = map(int,input().split())
    uv[u] = v


que = deque()
def bfs():
    while que:
        position = que.popleft()
        for roll in range(1,7):  # 주사위 1에서 6까지의 결과를 반복
            nextp = position + roll # 현재 위치에서 주사위 숫자 더하기
            if nextp <= 100: # 100을 넘지 않을경우에만
                if nextp in uv: # 사다리거나 뱀이면
                    if matrix[position]+1 < matrix[uv[nextp]]: # 사다리 타고 간 곳의 값이 이번턴에 간 횟수보다 작을때
                        matrix[uv[nextp]] = matrix[position]+1 # 그래프에 횟수 업데이트
                        que.append(uv[nextp])  # 업데이트 된곳에서 다시 주사위 돌리도록 큐에 추가
                else: # 사다리거나 뱀이 아닐때
                    if matrix[position]+1 < matrix[nextp]:  # 이미 방문했던 곳인지
                        matrix[nextp] = matrix[position]+1  # 업데이트
                        que.append(nextp) # 큐 추가
            if nextp == 100: # 100에 도달하면 끝
                return  

que.append(1)
bfs()
print(matrix[100])