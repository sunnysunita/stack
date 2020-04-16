from queue import Queue
from queue import LifoQueue
def inbuild_queue():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(q.get())
    print(q.get())
    print(q.empty())
    print(q.get())
    print(q.get())
    print(q.empty())

def inbuild_Stack():
    s = LifoQueue()
    s.put(1)
    s.put(2)
    s.put(3)
    s.put(4)
    print(s.get())
    print(s.empty())
    print(s.get())
    print(s.get())
    print(s.get())
    print(s.empty())


inbuild_Stack()
inbuild_queue()