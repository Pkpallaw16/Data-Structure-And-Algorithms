n1=int(input("eneter size of array"))
arr1=[]
n2=int(input("eneter size of array"))
arr2=[]
for i in range(n1):
    arr1.append(int(input()))
for i in range(n2):
    arr2.append(int(input()))
if n1>n2:
    rsize=n1+1
else:
    rsize=n2+1
res=[0 for i in range(rsize)]
i=n1-1
j=n2-1
carry=0
for k in range(rsize-1,-1,-1):
    if i >= 0:
        val1 = arr1[i]
    else:
        val1 = 0
    if j >= 0:
        val2 = arr2[j]
    else:
        val2 = 0
    sum=val1+val2+carry
    res[k]=sum%10
    carry=int(sum/10)
    i-=1
    j-=1
print(res)

