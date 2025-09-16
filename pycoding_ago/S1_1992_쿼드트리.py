import sys
input = sys.stdin.readline
n = int(input())
table = []
for i in range(n):
    table.append(list(input().strip()))
print(table)

# * 시작 x,y와 끝 x,y를 입력받고 step은 점점 줄어드는 제귀함수
def track(startx : int , starty:int, endx:int,  endy:int, step: int):
    temp = table[starty][startx] #* 시작점 값
    exitflag = False # * 이중 for문 나가는 변수
    for i in range(step):
        for k in range(step):
            if temp != table[startx][starty]: #* 시작점 값과 나머지 값이 다른지 확인
                exitflag = True
                break
        if exitflag:
            break
    if exitflag: #* 다른게 존재 한다면 S
        print("(",end="")
        step = step//2
        track(startx,starty,endx-step,endy-step,step)
        track(startx+step,starty,endx,endy-step,)