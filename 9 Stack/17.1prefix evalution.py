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
def prefix_evalution(expr):
    operand=[]
    for i in range(len(expr)-1,-1,-1):
        if expr[i]>='0' and expr[i]<='9':
            operand.append(int(expr[i]))
        else:
            val1=operand.pop()
            val2=operand.pop()
            res=evaluate(val1,val2,expr[i])
            operand.append(res)
    return operand.pop()
expr=input("input expr ")
print(prefix_evalution(expr))