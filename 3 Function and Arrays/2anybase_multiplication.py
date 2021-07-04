def anybase_addition(n1,n2,b):
    carry=0
    res=0
    pow=1
    while n1!=0 or n2!=0 or carry!=0:
        va11=n1%10
        n1=int(n1/10)
        val2=n2%10
        n2=int(n2/10)
        val=(va11+val2+carry)%b
        carry=int((va11+val2+carry)/b)
        res+=val*pow
        pow*=10
    return res
def anybase_multiplication(n1,n2,b):
    opow=1
    res=0
    while n1!=0:
        iva1=n1%10
        n1=int(n1/10)
        n2_copy=n2
        carry=0
        ipow=1
        pi = 0 #product on every level of multiplication
        while n2_copy!=0 or carry!=0:
            jval=n2_copy%10
            n2_copy=int(n2_copy/10)
            mult=iva1*jval+carry
            val = mult % b
            carry = int(mult / b)
            pi += val * ipow
            ipow *= 10
        pi *= opow
        opow *= 10
        res=anybase_addition(res,pi,b)
    return res
n1=int(input("entrt n1"))
n2=int(input("entrt n2"))
b=int(input("entrt base"))
print(anybase_multiplication(n1,n2,b))