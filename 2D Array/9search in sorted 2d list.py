def search_in_sorted_2dlist(arr,data):
    r=0
    c=len(arr[0])-1
    while r<len(arr) and c>=0:
        if arr[r][c]==data:
            print("(",r,c,")")
            return
        elif arr[r][c]<data:
            r+=1
        else:
            c-=1
    print("Not found")

n=int(input("eneter size of array"))
m=int(input("eneter size of array"))
arr=[[int(input()) for i in range(m)] for j in range(n)]
data=int(input("enter the number"))
search_in_sorted_2dlist(arr,data)