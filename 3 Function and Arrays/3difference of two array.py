n1=int(input("eneter size of array"))
arr1=[]
n2=int(input("eneter size of array"))
arr2=[]
for i in range(n1):
    arr1.append(int(input()))
for i in range(n2):
    arr2.append(int(input()))
i=n1-1
j=n2-1
carry=0
res=[]
for k in range(n2-1,-1,-1):
    if i >= 0:
        val1 = arr1[i]
    else:
        val1 = 0
    if j >= 0:
        val2 = arr2[j]
    else:
        val2 = 0
    sub=val2+carry-val1
    if sub<0:
        sub+=10
        carry=-1
    else:
        carry=0
    res.append(sub)
    i-=1
    j-=1
isleading_zero=True
for i in range(len(res)):
    if res[i]==0:
        if isleading_zero==True:
            isleading_zero = True
        else:
            print(res[i])

    else:
        print(res[i])
        isleading_zero=False

