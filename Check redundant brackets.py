list = input()
def fun(list):
    for i in range(0,len(list)):
        if list[i] == "(" and list[i+1] == ")":
            return True
        else:
            False

if fun(list) is True:
    print("true")
else:
    print("false")