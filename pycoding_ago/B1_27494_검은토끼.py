import sys
input = sys.stdin.readline
n = int(input())
ans = 0
def judge(a):
    a = list(str(a))
    for i in range(len(a)):
        if a[i] == '2':
            for j in range(i+1,len(a)):
                if a[j] == '0':
                    for k in range(j+1,len(a)):
                        if a[k] == '2':
                            for l in range(k+1,len(a)):
                                if a[l] == '3':
                                    return True
    return False


for i in range(2023,n+1):
    if judge(i):
        ans += 1
print(ans)