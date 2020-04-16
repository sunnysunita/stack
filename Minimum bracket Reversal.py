list = input()
def fun(list):
    s = []
    for e in list:
        if e is "{":
            s.append(e)

        elif e is "}":
            s.pop()
    # print(s)
    l = len(s)
    if l%2 != 0:
        return -1
    else:
        return l//2

print(fun(list))



