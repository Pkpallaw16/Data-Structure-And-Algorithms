def is_safe(chess,r,c):
    if r>=0 and c>=0 and r<len(chess) and c<len(chess) and chess[r][c]==0:
        return True
    else:
        return False
def knightsTour(chess,r,c,move):

    if move==len(chess)*len(chess):
        chess[r][c] = move
        print(move)
        print(chess)
        chess[r][c]=0
        return
    chess[r][c]=move
    rn=[-2,-1,1,2,2,1,-1,-2]
    cn=[-1,2,2,1,-1,-2,-2,-1]
    for i in range(8):
        if is_safe(chess,r+rn[i],c+cn[i]):
            knightsTour(chess,r+rn[i],c+cn[i],move+1)
    chess[r][c] = 0




n=int(input("size of chess "))
chess=[[0 for x in range(n)] for i in range(n)]
print(chess)
r=int(input("size of row "))
c=int(input("size of col"))
knightsTour(chess,r,c,1)