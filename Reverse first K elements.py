import queue
from sys import setrecursionlimit
setrecursionlimit(11000)
def reverseQueue(q1):
    if q1.qsize() == 1:
        return

    ele = q1.get()
    reverseQueue(q1)
    q1.put(ele)

def reverseFirstK(q1, q2, k):
    while k != 0:
        q2.put(q1.get())
        k -= 1

    """while q2.qsize() != 0:
        print(q2.get())"""
    """while q1.qsize() != 0:
        print(q1.get())"""

    reverseQueue(q2)
    """while q1.qsize() != 0:
        q1.get()"""
    """while q2.qsize() != 0:
        print(q2.get())"""

    while q1.qsize() != 0:
        q2.put(q1.get())
    """while q2.qsize() != 0:
        print(q2.get())"""
    return q2


#Implement Your Code Here


"""from sys import setrecursionlimit
setrecursionlimit(11000)"""
n = int(input())
li = [int(ele) for ele in input().split()]
k = int(input())
q = queue.Queue()
q2 = queue.Queue()
for ele in li:
    q.put(ele)

"""while q.qsize() != 0:
    print(q.get(), end=" ")"""

out = reverseFirstK(q, q2, k)
"""while out.qsize() != 0:
    print(out.get())"""
while(out.qsize()>0):
    print(out.get())
    n-=1
