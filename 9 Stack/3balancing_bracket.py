def isMatching(a, b):
    if (a == '(' and b == ')') or \
            (a == '{' and b == '}') or \
            (a == '[' and b == ']'):
        return True
    else:
        return False

def is_balanced_brackets(expr):
    stack=[]
    for x in expr:
        if x in ('(','{','['):
            stack.append(x)
        elif x in (')','}',']'):
            if not stack:
                return False
            elif isMatching(stack[-1],x)==False:
                return False
            else:
                stack.pop()
        else:
            continue

    if stack:
        return False
    else:
        return True
a = input()

print(is_balanced_brackets(a))