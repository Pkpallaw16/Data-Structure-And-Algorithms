import math
n=int(input("enter the num "))
for i in range(2,int(math.sqrt(n))+1):
    while n%i==0:
        print(i,end=" ")
        n=n/i

if n!=1:
    print(n)