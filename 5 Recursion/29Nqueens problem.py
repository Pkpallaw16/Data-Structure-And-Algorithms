def isItsSafePlaceForThequeen(chess, row,col):
    ndir=[-1,-1,-1]
    cdir=[0,-1,1]
    for i in range(1,row+1):
        for index in range(len(ndir)):
            nrow=row+ndir[index] *i
            ncol=col+cdir[index] *i
            #print(nrow,ncol)
            if nrow>=0 and ncol>=0 and nrow<len(chess) and ncol<len(chess) and chess[nrow][ncol] == 1:
                return False
    return True

def print_N_queens(chess,row,col,qpsf,asf):
    if row ==len(chess):
        if qpsf==len(chess):
            print(asf)
        return
    if col + 1 < len(chess[0]):
        # yes call
        if isItsSafePlaceForThequeen(chess,row,col):
            chess[row][col] = 1
            print_N_queens(chess,row + 1, 0,qpsf+1, asf + "(" + str(row) + "-" + str(col) + ")")
            chess[row][col] = 0
        # no call
        print_N_queens(chess,row, col + 1,qpsf, asf)

    else:
        # yes call
        if isItsSafePlaceForThequeen(chess, row, col):
            chess[row][col] = 1
            print_N_queens(chess,row + 1, 0,qpsf+1, asf + "(" + str(row) + "-" + str(col) + ")")
            chess[row][col] = 0
        # no call
        print_N_queens(chess,row + 1, 0,qpsf, asf)




n=int(input("enter matrix size"))
chess=[[0 for i in range(n)] for j in range(n)]
print_N_queens(chess,0,0,0,"")


