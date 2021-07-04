def anybase_subtraction(n1,n2,b):
    carry=0
    res=0
    pow=1
    while n2!=0:
        val2 = n2 % 10
        n2 = int(n2 / 10)
        va11=n1%10
        n1=int(n1/10)
        val=(val2+carry-va11)
        if val<0:
            val+=b
            carry=-1
        else:
            carry=0
        res+=val*pow
        pow*=10
    return res
n1=int(input("entrt n1"))
n2=int(input("entrt n2"))
b=int(input("entrt base"))
print(anybase_subtraction(n1,n2,b))