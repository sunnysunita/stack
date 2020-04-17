
import queue
class Queue_Using_Stack:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.count = 0

    def enQueue(self,data):
        self.s1.append(data)
        self.count += 1


    def deQueue(self):
        if self.count == 0:
            return "Empty Queue"
        else:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            self.e = self.s1.pop()
            while len(self.s2) >= 1:
                self.s1.append(self.s2.pop())
            self.count -= 1
            return self.e


    def front(self):
        if self.count == 0:
            return "Empty Queue"
        else:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            self.e = self.s1.pop()
            self.s1.append(self.e)
            while len(self.s2) >= 1:
                self.s1.append(self.s2.pop())
            return self.e


    def getSize(self):
        return self.count


q = Queue_Using_Stack()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.enQueue(50)
while q.getSize() is not 0:
    print(q.deQueue())


"""li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')

    i+=1"""






