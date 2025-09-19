import sys
input = sys.stdin.readline

dic = {'A':'000000','B':'001111', 'C':'010011','D' : '011100',
'E' : '100110',
'F' : '101001',
'G' : '110101',
'H' : '111010'}

n = int(input())
stri = input().rstrip()
for i in range(n):
    stri[0+i*6:6+i*6] =