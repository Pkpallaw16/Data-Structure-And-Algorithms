def prefix_to_infix(expr):
    operand=[]
    for i in range(len(expr)-1,-1,-1):
        if expr[i]>='0' and expr[i]<='9':
            operand.append(expr[i])
        else:
            val1=operand.pop()
            val2=operand.pop()
            res='('+val1+expr[i]+val2+')'
            operand.append(res)
    return operand.pop()
expr=input("input expr ")
print(prefix_to_infix(expr))