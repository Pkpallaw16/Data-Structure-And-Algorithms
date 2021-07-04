import math
n=int(input("enter first num "))
m=int(input("enter 2nd num "))
flag=0
for i in range(n,m+1):
    for div in range(2,int(math.sqrt(i))+1):
        if i%div==0:
            flag=1
            break
    if flag==0:
        print(i)
    flag=0
