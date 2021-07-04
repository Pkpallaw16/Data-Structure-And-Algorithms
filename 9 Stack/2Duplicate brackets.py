

def duplicate_paranthesis(exper):
    stack = []
    for x in exper:
        if x !=')':
            stack.append(x)

        else:
            if stack[-1]=='(':
                return True
            while stack[-1]!='(':
                stack.pop()
    return False

a = input("enter expr ")

print(duplicate_paranthesis(a))
