
def saddle_point(arr):
    for r in range(len(arr)):
        min_col_index=arr[r].index(min(arr[r]))
        print(arr[r])
        col=[row[min_col_index] for row in arr]
        print(col)
        max_row_index=col.index(max(col))
        if max_row_index==r:
            print("saddle point",arr[r][min_col_index])
            return
    print("no saddle point")



n=int(input("eneter size of array"))
m=int(input("eneter size of array"))
arr=[[int(input()) for i in range(m)] for j in range(n)]
saddle_point(arr)
print(arr)