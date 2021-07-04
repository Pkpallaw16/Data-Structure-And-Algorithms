def exit_point(arr):
    r=0
    c=0
    dir=0
    while r>=0 and r<len(arr) and c>=0 and c<len(arr[0]):
        dir=(dir+arr[r][c])%4
        if dir==0:
            c+=1
        elif dir==1:
            r+=1
        elif dir==2:
            c-=1
        else:
            r-=1
    if dir == 0:
        c -= 1
    elif dir == 1:
        r -= 1
    elif dir == 2:
        c += 1
    else:
        r += 1

    print(r,c)
arr=[[0,0,1,0],[0,0,0,0],[0,0,0,0],[1,0,1,0]]
exit_point(arr)