import sys
input = sys.stdin.readline

#* 입력 받기
n = int(input())
lis = list(map(int,input().split()))

dp = [1]*n # dp 설정
ans = [[i] for i in lis] # 출력할 문자열 : 초기값은 입력받은 문자열로 가지는 2중 배열
#? 예시 lis가 [3,4,7,2]면 ans는 [[3], [4], [7], [2]]
indx = 0 # dp에서 가장 큰값 찾는 인덱스
ansnum = 0 #dp에서 가장 큰값을 저장
for i in range(n): #
    for k in range(i+1): #! i+1안해도 될거 같음
        if lis[i] > lis[k] and dp[i] < dp[k]+1: # 숫자가 증가하고 그 전꺼에서 dp가 커지는지
            dp[i] = dp[k]+1
            ans[i] = ans[k]+[lis[i]]  #* 문자열 
    if ansnum<dp[i]: #* 매 단계마다 dp 최대 값인지
        ansnum = dp[i]
        indx = i
print(ansnum)
print(*ans[indx])