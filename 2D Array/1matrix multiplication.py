n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
m1=int(input("eneter size of array"))
m2=int(input("eneter size of array"))
arr2=[[int(input()) for i in range(n2)] for j in range(n1)]
arr3=[[0 for i in range(m2)] for j in range(n1)]
if n2!=m1:
    print("matrix cannot be multiplied")
else:
    for i in range(len(arr3)):
        for j in range(len(arr1)):
            sum=0
            for j in range(m1):
                sum+=arr1[i][j]*arr2[j][i]
            arr3[i][j]=sum
print(arr3)
