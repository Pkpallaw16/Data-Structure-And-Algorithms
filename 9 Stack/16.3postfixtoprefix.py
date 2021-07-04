def postfix_prefix(expr):
    operand = []
    for x in expr:
        if x >= '0' and x <= '9':
            operand.append(x)
        else:
            val2 = operand.pop()
            val1 = operand.pop()
            res = x+val1+val2
            operand.append(res)
    return operand.pop()


expr = input("input expr ")
print(postfix_prefix(expr))