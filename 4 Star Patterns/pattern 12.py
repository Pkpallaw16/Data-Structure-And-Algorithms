n=int(input("enter num "))
a=0
b=1
for r in range(1,n+1):
    for c in range(1,r+1):
        print(a,end=" ")
        sum=a+b
        a=b
        b=sum
    print()