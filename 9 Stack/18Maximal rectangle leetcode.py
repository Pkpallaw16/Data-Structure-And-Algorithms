import largest_area_histogram as lsh
def maximal_rectange(matrix):
    if len(matrix)==0 or len(matrix[0])==0:
        return 0
    arr=[0 for i in range(len(matrix[0]))]
    res=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='0':
                arr[j]=0
            else:
                arr[j]+=int(matrix[i][j])
        print(arr)
        max_till_row=lsh.largest_area_histogram(arr)
        print(max_till_row)
        res=max(res,max_till_row)
    return res
mat=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximal_rectange(mat))
