import sys
input = sys.stdin.readline


def loop(lis:list,start:int,chosen:list):
    if len(chosen)==6:
        print(' '.join(map(str, chosen)))
        return
    for i in range(start, len(lis)):
        chosen.append(lis[i])
        loop(lis, i+1, chosen)
        chosen.pop()
    

while(True):
    input_data = list(map(int, input().split()))
    if input_data[0] == 0:
        break
    k, S = input_data[0], input_data[1:]
    loop(S, 0, [])
    print()

