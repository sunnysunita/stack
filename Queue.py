class Queue:
    def __init__(self):
        self.list = []
        self.count = 0
        self.front = 0

    def enQueue(self,data):
        self.list.append(data)
        self.count += 1

    def deQueue(self):
        if self.count == 0:
            return
        else:
            self.e = self.list[self.front]
            self.front += 1
            self.count -= 1
            return self.e

    def frontfun(self):
        if self.count == 0:
            return
        else:
            return self.list[self.front]

    def size(self):
        return self.count

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False


q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print(q.size())
print(q.isEmpty())
print(q.deQueue())
print(q.deQueue())
print(q.frontfun())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.isEmpty())