
def flood_fill(arr,row,col,psf,visited):
    if row<0 or col<0 or row==len(arr) or col==len(arr[0]) or arr[row][col]==1 or visited[row][col]==True:
        return
    if row==len(arr)-1 and col==len(arr[0])-1:
        print(psf)
        return
    visited[row][col]=True
    flood_fill(arr,row-1,col,psf+"t",visited)
    flood_fill(arr, row, col-1, psf + "l",visited)
    flood_fill(arr, row + 1, col, psf + "d",visited)
    flood_fill(arr, row , col+1, psf + "r",visited)
    visited[col][row]=False

m=int(input("Enter row size"))
n=int(input("enter column size"))
visited=[[False for i in range(n)] for j in range(n)]
arr=[[0 for i in range(n)] for j in range(n)]
for i in range(m):
    a =input().split()
    for j in range(n):
         arr[i][j]=int(a[j])

print(arr)

flood_fill(arr,0,0,"",visited)


