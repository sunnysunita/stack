n = int(input())
s1 = [int(e) for e in input().split()]
s2 = []
def reverse_stack(s1, s2):
    if len(s1) == 1:
        return
    for i in range(1, len(s1)):
        s2.append(s1.pop())
    temp = s1.pop()
    for i in range(0,len(s2)):
        s1.append(s2.pop())
    reverse_stack(s1, s2)
    s1.append(temp)

reverse_stack(s1, s2)
for i in range(0, len(s1)):
    print(s1.pop(), end=" ")



