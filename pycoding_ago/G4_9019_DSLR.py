from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def D(a:int):
    return (a*2)%10000
def S(a:int):
    if a == 0:
        return 9999
    return a-1
def L(a:int):
    a = (a % 1000)*10+a//1000
    return a
def R(a:int):
    a = (a // 10) + (a % 10)*1000
    return a

def BackS(a):
    if a == 9999:
        return 0
    return a+1
def BackL(a):
    return R(a)
def BackR(a):
    return L(a)
oplist = ["D","S","L","R"]

def opFuclist(i : int, num:int):
    if i == 0:
        return D(num)
    elif i ==1:
        return S(num)
    elif i ==2:
        return L(num)
    else:
        return R(num)

def bfs(a,b):
    frontque = deque()
    backque = deque()
    frontque.append((a,""))
    frontdic[a] = ""
    backdic[b] = ""
    backque.append((b,""))
    fstage = 1
    bstage = 1
    while frontque or backque:  # 반복 진행 부분
        #print(f"back{backdic} \n\n front{frontdic} \n\n")
        
        while True:
            frontnum,frontop = frontque.popleft() # 큐에서 원소 하나 꺼냄
            if len(frontop) >= fstage:
                frontque.appendleft((frontnum,frontop))
                break
            for i in range(4): # DSLR 반복 
                frodslr = opFuclist(i,frontnum)
                if frodslr not in frontdic: # 전에 있던 수가 아니라 다른 수 일때
                    frontdic[frodslr] = frontop+oplist[i] # 방문했다고 dic에 표시

                    if frodslr in backdic: # 백으로 찾은것과 만났을 때
                        return frontdic[frodslr]+backdic[frodslr]

                    frontque.append((frodslr,frontdic[frodslr])) # 큐에 추가
        fstage+=1
        # 백으로 한단계 진행
        while True:
            backnum,backop = backque.popleft()
            if len(backop)>=bstage:
                backque.appendleft((backnum,backop))
                break
            # D 부분
            if backnum %2 ==0: 
                d1 = backnum //2
                d2 = d1+5000
                if d1 not in backdic: # 전에 있던 수가 아니라 다른 수 일 때
                    backdic[d1] = "D"+backop # 방문 했다고 dic에 추가
                    backque.append((d1,"D"+backop)) # 큐에 추가 (^^| 나중에 str+로 시가초과 발상 가능성 있음)
                    if d1 in frontdic:

                        return frontdic[d1]+backdic[d1]

                if d2 not in backdic:
                    backdic[d2] = "D"+backop
                    backque.append((d2,"D"+backop)) # 큐에 추가
                    if d2 in frontdic:

                        return frontdic[d2]+backdic[d2]

            # S 부분
            s = BackS(backnum)
            if s not in backdic:
                backdic[s] = "S"+backop
                backque.append((s,"S"+backop)) # 큐에 추가
                if s in frontdic:
                    return frontdic[s]+backdic[s]
            # L 부분
            l = BackL(backnum)
            if l not in backdic:
                backdic[l] = "L"+backop
                backque.append((l,"L"+backop)) # 큐에 추가
                if l in frontdic:
                    return frontdic[l]+backdic[l]
            # R 부분
            r = BackR(backnum)
            if r not in backdic:
                backdic[r] = "R"+backop
                backque.append((r,"R"+backop)) # 큐에 추가
                if r in frontdic:
                    return frontdic[r]+backdic[r]
        bstage+=1




        

for _ in range(t):
    a,b = map(int,input().split())
    frontdic = {}
    backdic = {}
    print(bfs(a,b))
