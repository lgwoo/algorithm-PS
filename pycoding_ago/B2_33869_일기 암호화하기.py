import sys
from collections import deque
input = sys.stdin.readline

w = list(input().strip())
setw = set()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keys = list(sorted(list(set(alpha[:]) - set(w)),reverse=True))
w = deque(w)
dic = dict()
i = 0
while w:
    aa = w.popleft()
    if aa in setw:
        continue
    dic[alpha[i]] = aa
    setw.add(aa)
    i+=1

for i in range(len(setw),26):
    dic[alpha[i]] = keys.pop()

s = input().strip()
for i in s:
    print(dic[i],end="")