class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.__list = []
        self.__count = 0
        self.__head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1



    def pop(self):
        self.__head = self.__head.next
        self.__count -= 1

    def top(self):
        print(self.__head.data)

    def size(self):
        print(self.__count)

    def isEmpty(self):
        if self.__count == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")

s = Stack()
s.push(10)
s.top()
s.isEmpty()