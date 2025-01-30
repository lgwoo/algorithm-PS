want = ["banana","apple","rice", "pork", "pot"]
number =[3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

def solution(want,number,discount):
    answer = 0
    wantitem = []
    for i in range(len(want)):
        for _ in range(number[i]):
            wantitem.append(want[i])
    
    for i in range(len(discount)-9):
        if sorted(wantitem) == sorted(discount[i:i+10]):
            answer+=1

            
solution(want,number,discount)