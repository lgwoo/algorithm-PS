import sys
input = sys.stdin.readline

dic = {'A':'000000','B':'001111', 'C':'010011','D' : '011100',
'E' : '100110',
'F' : '101001',
'G' : '110101',
'H' : '111010'}
flag = 0
anss = ''
n = int(input())
stri = input().rstrip()
breakpoint = 0
for i in range(n): # 큰 단위
    clearpoint = 0
    for j in dic: # 딕셔너리 알파벳 비교
        flag = 0
        for k in range(6): # 6글자 비교
            if stri[0+i*6+k] != dic[j][k]:
                flag += 1
                if flag > 1:
                    break
        if flag <= 1:
            anss += j
            clearpoint = 1
            break
    if clearpoint == 1:
        continue
    else:
        breakpoint = i+1
        break
if len(anss) == n:
    print(anss)
else:
    print(breakpoint)

