import sys
import heapq  # 힙을 사용하기 위해
input = sys.stdin.readline

heap = [] # 일반리스트처럼씀 but push pop 함수만 다르게

n = int(input())
for i in range(n):
    k = int(input())
    if k != 0:
        heapq.heappush(heap,-k)  # 보통은 최소 힙이기 때문에 최대힙처럼 하기위해 부호 반전
    elif len(heap)==0:
        print(0)
    else:
        print(-heapq.heappop(heap))
        
