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
def posfix_evalution(expr):
    operand=[]
    for x in expr:
        if x>='0' and x<='9':
            operand.append(int(x))
        else:
            val2=operand.pop()
            val1=operand.pop()
            res=evaluate(val1,val2,x)
            operand.append(res)
    return operand.pop()
expr=input("input expr ")
print(posfix_evalution(expr))