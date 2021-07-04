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
n1=int(input("entrt n1"))
n2=int(input("entrt n2"))
b=int(input("entrt base"))
print(anybase_addition(n1,n2,b))