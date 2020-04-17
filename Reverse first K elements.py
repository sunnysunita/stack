import queue

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

    reverseQueue(q2)
    while q2.qsize() != 0:
        q2.get()
    """while q1.qsize() != 0:
        q2.put(q1.get())"""


#Implement Your Code Here


from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
q2 = queue.Queue()
for ele in li:
    q.put(ele)
k = int(input())
reverseFirstK(q, q2, k)
"""while(q.qsize()>0):
    print(q.get())
    n-=1"""