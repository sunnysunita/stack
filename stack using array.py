class Stack:
    def __init__(self):
        self.__list = []
    def push(self,data):
        self.__list.append(data)

    def pop(self):
        self.__list.pop()

    def top(self):
        print(self.__list[len(self.__list)-1])
        pass

    def size(self):
        print(len(self.__list))

    def isEmpty(self):
        if len(self.__list) == 0:
            print("yes, list is Empty")
        else:
            print("No, list is not Empty")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.size()
s.top()
s.pop()
s.top()
s.isEmpty()
s.size()
