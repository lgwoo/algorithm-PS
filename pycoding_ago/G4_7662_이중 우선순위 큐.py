import sys
import heapq
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    min_heap = []
    max_heap = []
    k = int(input())
    visited = [False]*k
    for i in range(k):
        op,num = input().split()
        num = int(num)
        
        if op == "I":
            heapq.heappush(min_heap,(num,i))
            heapq.heappush(max_heap,(-num,i))
        elif len(max_heap)>0 and len(min_heap)>0:

            if num == -1:
                while len(min_heap)>0 and visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if len(min_heap)>0:
                    temp = heapq.heappop(min_heap)
                    visited[temp[1]] = True
            else:
                while len(max_heap)>0 and visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if len(max_heap)>0:
                    temp = heapq.heappop(max_heap)
                    visited[temp[1]] = True
    while len(max_heap)>0 and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while len(min_heap)>0 and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if len(min_heap)==0 or len(max_heap)==0:
        print("EMPTY")
    else:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(max_heap)
        print(f"{-b[0]} {a[0]}")


'''
perplexity의 개선 코드
```
import sys
import heapq
input = sys.stdin.readline

def clean_heap(heap, deleted):
    while heap and heap[0][1] in deleted:
        heapq.heappop(heap)

t = int(input())

for _ in range(t):
    min_heap, max_heap = [], []
    deleted = set()
    count = 0
    
    for _ in range(int(input())):
        op, num = input().split()
        num = int(num)
        
        if op == 'I':
            heapq.heappush(min_heap, (num, count))
            heapq.heappush(max_heap, (-num, count))
            count += 1
        elif count > len(deleted):  # 큐에 원소가 있을 때만 삭제 연산 수행
            if num == 1:
                clean_heap(max_heap, deleted)
                if max_heap:
                    deleted.add(heapq.heappop(max_heap)[1])
            else:
                clean_heap(min_heap, deleted)
                if min_heap:
                    deleted.add(heapq.heappop(min_heap)[1])

    clean_heap(max_heap, deleted)
    clean_heap(min_heap, deleted)

    if len(max_heap) == 0:
        print("EMPTY")
    else:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")


'''