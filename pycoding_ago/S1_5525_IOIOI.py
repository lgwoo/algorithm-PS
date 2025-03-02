import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

iostr = "I" + "OI"*n
ioilen = 1+2*n
count = 0
i = 0
while i < m:
    if s[i] == "I":
        Ocount = 0
        while(s[i+1:i+3] == "OI"):
            Ocount +=1
            if i + 2 < m:
                i +=2
            else:
                break
        if Ocount - n + 1 > 0:
            count+= Ocount-n+1
    i+=1        
print(count)