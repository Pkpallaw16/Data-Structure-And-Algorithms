def recursion():
    r=10
    c=10
    rdir=[-1,0,1,0]
    cdir=[0,1,0,-1]
    radius=1
    for rad in range(1,radius+1):
        for i in range(len(rdir)):
            nr=r+rad*rdir[i]
            nc=c+rad*cdir[i]
            print(nr,nc)

    print("..................")
    for i in range(len(rdir)):
        for rad in range(1,radius+1):
            nr=r+rad*rdir[i]
            nc=c+rad*cdir[i]
            print(nr,nc)