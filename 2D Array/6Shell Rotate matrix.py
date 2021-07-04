def filloned_fromshell(arr,shell):
    r_start = shell - 1
    r_end = len(arr) - shell
    c_start = shell - 1
    c_end = len(arr[0]) - shell
    sz=2*(r_end-r_start+c_end-c_start)
    oned=[]
    for i in range(r_start, r_end+1):
        oned.append(arr[i][c_start])
    c_start += 1

    for i in range(c_start, c_end + 1):
        oned.append(arr[r_end][i])
    r_end -= 1

    for i in range(r_end, r_start - 1, -1):
        oned.append(arr[i][c_end])
    c_end -= 1

    for i in range(c_end, c_start - 1, -1):
        oned.append(arr[r_start][i])
    r_start += 1
    return oned
def fillshell_fromoned(arr,shell,oned):
    r_start = shell - 1
    r_end = len(arr) - shell
    c_start = shell - 1
    c_end = len(arr[0]) - shell
    sz = 2 * (r_end - r_start + c_end - c_start)
    for i in range(r_start, r_end + 1):
        arr[i][c_start]=oned.pop(0)
    c_start += 1

    for i in range(c_start, c_end + 1):
        arr[r_end][i]=oned.pop(0)
    r_end -= 1

    for i in range(r_end, r_start - 1, -1):
        arr[i][c_end]=oned.pop(0)
    c_end -= 1

    for i in range(c_end, c_start - 1, -1):
        arr[r_start][i]=oned.pop(0)
    r_start += 1
    print(arr)
def reverse_arr(oned,li,ri):
    while li<ri:
        oned[li],oned[ri]=oned[ri],oned[li]
        li+=1
        ri-=1
def rotate_array(oned,r):
    r=r%len(oned)
    if r<0:
        r=r+len(oned)
    reverse_arr(oned,0,len(oned)-r-1)
    reverse_arr(oned,len(oned)-r,len(oned)-1)
    reverse_arr(oned,0,len(oned)-1)


def Shell_Rotate_matrix_2nd(arr,shell,rotate):
    oned=filloned_fromshell(arr,shell)
    print(oned)
    rotate_array(oned,rotate)
    print(oned)
    fillshell_fromoned(arr,shell,oned)
def Shell_Rotate_matrix(arr,shell,rotate):
    r_start=shell-1
    r_end=len(arr)-shell
    c_start=shell-1
    c_end=len(arr[0])-shell
    while rotate>0:
        temp=arr[r_end][c_start]

        for i in range(r_end,r_start,-1):
            arr[i][c_start]=arr[i-1][c_start]
        c_start+=1

        for i in range(c_start,c_end+1):
            print(arr[r_end][i],temp)
            arr[r_end][i],temp=temp,arr[r_end][i]
            print(arr[r_end][i], temp)
        r_end-=1

        for i in range(r_end,r_start-1,-1):
            arr[i][c_end],temp=temp,arr[i][c_end]
        c_end-=1

        for i in range(c_end,c_start-1,-1):
            arr[r_start][i],temp=temp,arr[r_start][i]
        r_start+=1

        arr[r_start-1][c_start-1]=temp
        r_start = shell - 1
        r_end = len(arr) - shell
        c_start = shell - 1
        c_end = len(arr[0]) - shell
        rotate-=1
    print(arr)


n1=int(input("eneter size of array"))
n2=int(input("eneter size of array"))
arr1=[[int(input()) for i in range(n2)] for j in range(n1)]
print(arr1)
#Shell_Rotate_matrix(arr1,2,3)
Shell_Rotate_matrix_2nd(arr1,2,3)
print(arr1)

