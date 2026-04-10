import sys
input = sys.stdin.readline
n,l = map(int,input().split())

lis = list(map(int,input().split())) # 물 떨어지는 위치 입력 받기
loca = [False]*1001 # 지도에 물떨어지는 위치 표시할 리스트 (더 개선 한다면
                    # 물떨어지는 위치의 최대값까지로 크기제한 가능)

for i in lis:
    loca[i] = True # 지도에 물떨어지는 위치 표시
ans = 0

for i in range(len(loca)): # 지도 순회
    if loca[i] == True: # 물떨어지는 위치라면
        if i+l >= 1001: # 끝쪽이면
            ans+=1 
            break # 종료
        for k in range(l): # 끝이 아니라면 판자 길이만큼을 물 떨어지지 않는 것으로 표시
            loca[i+k] = False
        ans+=1

# 시간 복잡도 O(n*l) 일듯?
print(ans)