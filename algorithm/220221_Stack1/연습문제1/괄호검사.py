# (), {} 검사

input_string = "((((){}{})))"
stack = []
for char in input_string:
    if char == "(" or char == "{":
        stack.append(char)
    elif char == ")":
        if len(stack) > 0:
            if stack[-1] == char:
                stack.pop()
            else:
                print("오류")
                break

        else:
            print("오류")
            break

    elif char == "}":
        if len(stack) > 0:
            if stack[-1] == char:
                stack.pop()
            else:
                print("오류")
                break

        else:
            print("오류")
            break

if len(stack) > 0:
    print("오류")