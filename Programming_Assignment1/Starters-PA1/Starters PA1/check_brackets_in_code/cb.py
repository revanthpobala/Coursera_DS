def check_brackets(data):
    stack = []
    balanced = True
    index = 0
    while index < len(data) and True:
        _value = data[index]
        if _value in ["(", "["]:
            stack.append(_value)
        else:
            if len(stack) == 0:
                balanced = False
            else:
                top = stack.pop()
                if top == "[" and _value!= "]" or top == "(" and _value!= ")":
                    balanced = False
        index += 1

    if balanced and len(stack) == 0:
        return True
    else:
        return False


data = "}()"
print check_brackets(data)
