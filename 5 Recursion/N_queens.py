def isItsSafePlaceForTheQueen(chess, row,col):
    for i in range(row-1,-1,-1):
        if chess[i][col]==1:
            return False

    r=row-1
    c=col-1
    while r>=0 and c>=0:
        if chess[r][c]==1:
            return False
        r -=1
        c -=1
    r1=row-1
    c1=col+1
    while r1>=0 and c1<len(chess):
        if chess[r1][c1]==1:
            return False
        r1 -=1
        c1 +=1
    return True
def print_N_queens(chess,qsf,row):
    if row ==len(chess):
        print(qsf)
        return
    for col in range(len(chess)):
        if isItsSafePlaceForTheQueen(chess,row,col)==True:
            chess[row][col] = 1
            print_N_queens(chess, qsf + str(row) + "-" + str(col) + ",", row + 1)
            chess[row][col] = 0



n=int(input("enter matrix size"))
chess=[[0 for i in range(n)] for j in range(n)]
print_N_queens(chess,"",0)


