def evaluate(val1,val2,op):
    if op=='+':
        val=val1+val2
    elif op=='-':
        val=val1-val2
    elif op=='*':
        val=val1*val2
    elif op=='/':
        val=val1/val2
    else:
        val=val1**val2
    print(val,op)
    return val



def infix_evalution(expr):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operator=[]
    operands=[]
    for x in expr:
        if x==' ':
            continue
        elif x>='0' and x<='9':
            operands.append(int(x))
        elif x=='(':
            operator.append(x)
        elif x==')':
            while operator[-1]!='(':
                val2 = operands.pop()
                val1 = operands.pop()
                op = operator.pop()
                val = evaluate(val1, val2, op)
                operands.append(val)
            operator.pop()
        else:
            while len(operator)>0 and operator[-1]!='(' and precedence[operator[-1]]>=precedence[x]:
                val2 = operands.pop()
                val1 = operands.pop()
                op = operator.pop()
                val = evaluate(val1, val2, op)
                operands.append(val)
            operator.append(x)

    if len(operator)>0:
        val2 = operands.pop()
        val1 = operands.pop()
        op = operator.pop()
        val = evaluate(val1, val2, op)
        operands.append(val)
    return operands.pop()
expr=input("enter expression")
print(infix_evalution(expr))
