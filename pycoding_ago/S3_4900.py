import sys
input = sys.stdin.readline
dic = {
    "063" : "0",
    "010" : "1",
    "093" : "2",
    "079" : "3",
    "106" : "4",
    "103" : "5",
    "119" : "6",
    "011" : "7",
    "127" : "8",
    "107" : "9"}

num_to_seg = {v: k for k, v in dic.items()}


string = input().strip()
while string != "BYE":
    a = ""
    b = ""
    strings = string.split("+")
    for i in range(len(strings[0])//3):
        a += dic[strings[0][i*3:i*3+3]]
    for i in range(len(strings[1])//3):
        b += dic[strings[1][i*3:i*3+3]]
    c = str(int(a)+int(b))
    c_seg = "".join(num_to_seg[ch] for ch in c)
    print(string+c_seg)
    string = input().strip()
