import math
n=int(input("enter the number "))
k=int(input("enter the rotation"))
temp=n
digits=0
while temp>0:
    digits+=1
    temp=int(temp/10)
k=k%digits
if k<0:
    k=digits+k
rotation=math.pow(10,k)
remdigits=math.pow(10,digits-k)
num_to_rotate=int(n%rotation)
rem_num=int(n/rotation)
rotated_num=num_to_rotate*remdigits+rem_num
print(int(rotated_num))

