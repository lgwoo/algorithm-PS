import sys
input = sys.stdin.readline

p = int(input())
for pp in range(p):
    ans = 0
    plis = list(map(int,input().split()))
    lis = plis[1:]
    for i in range(1,12):
        if lis[i]>lis[i-1]:
            for k in range(i,12):
                if lis[i-1]<min(lis[i:k+1]) and lis[k+1]< min(lis[i:k+1]):
                    #print(f"ans{i,k}")
                    ans+=1
                    
    print(pp+1,ans)
