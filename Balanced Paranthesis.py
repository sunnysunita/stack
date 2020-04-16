list = input()
def fun(list):
    s = []
    for e in list:
        if e in ["[", "{", "("]:
            s.append(e)

        elif e in ["]", "}", ")"]:
            if len(s) == 0:
                return False

            top = s[len(s)-1]
            if top == "[" and e == "]":
                s.pop()
            elif top == "{" and e == "}":
                s.pop()
            elif top == "(" and e == ")":
                s.pop()
            else:
                return False
    if len(s) == 0:
        return True
    else:
        return False

if fun(list) is True:
    print("true")
else:
    print("false")
"""{ a + [ b + ( c + d ) ] + ( e + f ) }"""


