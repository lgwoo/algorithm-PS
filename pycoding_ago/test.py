a = int(input())
plat = [["*" for i in range(a)] for i in range(a)]


def loop(startx,starty,size):
    ls = int(size/3)
    for i in range(ls):
        for j in range(ls):
            plat[startx+ls+i][starty+ls+j] = " "

    if ls == 1:
        return
    loop(startx, starty, ls)
    loop(startx+ls, starty, ls)
    loop(startx+ls*2, starty, ls)

    loop(startx, starty+ls, ls)

    loop(startx+ls*2,starty+ls, ls)

    loop(startx, starty+ls*2, ls)
    loop(startx+ls, starty+ls*2, ls)
    loop(startx+ls*2, starty+ls*2, ls)


loop(0,0,a)

for i in plat:
    print(*i,sep='')