import math
import random
n=int(input("enter first num "))
hi=int(input("enter first num "))
list=[random.randrange(1, hi, 1) for i in range(n)]

isprime=[True for i in range(hi+1)]

for i in range(2,int(math.sqrt(hi))+1):
    if isprime[i]:
        for j in range(i+i,hi+1,i):
            isprime[j]=False
print(isprime)
for i in range(len(list)):
    num=list[i]
    if num==0 or num==1:
        continue
    if isprime[num]==True:
        print(list[i],"is prime")
    else:
        print(list[i], "is not prime")

