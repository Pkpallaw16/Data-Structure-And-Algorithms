def Exit_point_of_matrix(arr):
    i=0
    j=0
    while True:
        dir=(dir+arr[i][j])%4
        if dir==0:
            j+=1
        elif dir==1:
            i+=1
        elif dir==2:
            j-=1
        elif dir==3:
            i-=1
        if i<0:
            i+=1
            break
        elif j<0:
            j+=1
            break
        elif i==len(arr):
            i-=1
            break
        elif j==len(arr[0]):
            j-=1
            break
n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
print(arr1)
Exit_point_of_matrix(arr1)