import sys
input = sys.stdin.readline
lis = input().split()

a = int(eval(f"int({lis[0]}{lis[1]}{lis[2]}){lis[3]}{lis[4]}"))
b = int(eval(f"{lis[0]}{lis[1]}int({lis[2]}{lis[3]}{lis[4]})"))
print(min(a,b))
print(max(a,b))
