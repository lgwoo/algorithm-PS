import sys
input = sys.stdin.readline
n = int(input())
lis = []

for _ in range(n):
    lis.append(tuple(map(int,input().split())))
lis.sort() # 정렬했기 때문에 시작시간은 항상 그 다음것보다 일찍임
anslis = []
for i in lis:
    if  len(anslis)==0:
        anslis.append(i)
    elif anslis[-1][1] > i[1]: # 그전의 종료시간이 현재의 종료시간보다 클때(그전걸 지워야할때)
        anslis.pop()
        anslis.append(i)
    elif anslis[-1][1]<=i[0]: #그전의 종료시간이 현재의 시작 시간보다 작을때(그냥 추가하면됌)
        anslis.append(i)

print(len(anslis))