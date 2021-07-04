n=int(input("enter num1 "))
m=int(input("rnter num2 "))
divisor=n
dividend=m
while divisor%dividend!=0:
    rem=divisor%dividend
    divisor=dividend
    dividend=rem
gcd=m
lcm=(n*m)/gcd
print(gcd,lcm)
