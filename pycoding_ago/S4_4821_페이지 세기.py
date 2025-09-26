import sys
input = sys.stdin.readline


def twocound(string: str):
    global book
    string = string.split('-')
    start = int(string[0])
    end = int(string[1])
    for i in range(start, min(end+1,page+1)):
        book[i] = 1
    return

n = int(input())

while n !=0 :
    page = n
    book = [0]*(page+1)
    order = input().split(',')
    for i in order:
        if '-' in i:
            twocound(str(i))
        else:
            if int(i) <= page:
                book[int(i)] = 1
    print(sum(book))
    n = int(input())
