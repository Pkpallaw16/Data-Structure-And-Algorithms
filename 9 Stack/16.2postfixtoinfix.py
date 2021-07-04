def postfix_to_infix(expr):
    operand = []
    for x in expr:
        if x >= '0' and x <= '9':
            operand.append(x)
        else:
            val2 = operand.pop()
            val1 = operand.pop()
            res = '('+ val1+x+val2+')'
            operand.append(res)
    return operand.pop()


expr = input("input expr ")
print(postfix_to_infix(expr))