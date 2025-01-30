import sys
input = sys.stdin.readline


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.tail = Node('tail')
        self.head = Node('head')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.cursor
        new_node.prev = self.cursor.prev
        self.cursor.prev.next = new_node
        self.cursor.prev = new_node
    def Lcommand(self):
        if self.cursor.prev.prev:
            self.cursor = self.cursor.prev 
    def Dcommand(self):
        if self.cursor.next:
            self.cursor = self.cursor.next
    def Bcommand(self):
        if self.cursor.prev.prev:
            backnode:Node = self.cursor.prev
            bbnode:Node = backnode.prev
            bbnode.next = self.cursor
            self.cursor.prev = bbnode
    def get_text(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            current = current.next
        return ''.join(result)

llist = LinkedList()


abc = input().strip()
for i in abc:
    llist.insert(i)

m = int(input())
order = [0]*m
for i in range(m):
    x = input().strip()
    order[i] = x



for x in order:
    if x=='L':
        llist.Lcommand()
    elif x=="D":
        llist.Dcommand()
    elif x=="B":
        llist.Bcommand()
    else:
        _,a = x.split()
        llist.insert(a)
        
print(llist.get_text())

### 이중연결리스트가 아니라 리스트 두개로 pop명령어로 
# 커서왼쪽과 오른쪽을 나눠서 할수도 있음
