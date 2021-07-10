class Orange_pair:
    def __init__(self, x,y,t):
        self.x=x
        self.y=y
        self.t=t
def rotten_orange(grid):
    st=[]
    fresh_orange=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==2:
                st.append(Orange_pair(i,j,0))
                fresh_orange+=1
            elif grid[i][j]==1:
                fresh_orange+=1
    xdir=[-1,0,1,0]
    ydir=[0,-1,0,1]
    time=-1
    while len(st)>0:
        size=len(st)
        while size>0:
            remove=st.pop(0)
            if grid[remove.x][remove.y]==-1:
                continue
            grid[remove.x][remove.y]=-1
            time=remove.t
            print("orange at","[",remove.x,",",remove.y,"]","rotted at time",remove.t)
            fresh_orange-=1
            for d in range(len(xdir)):
                r=remove.x+xdir[d]
                c=remove.y+ydir[d]
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1:
                    st.append(Orange_pair(r,c,remove.t+1))
            size-=1

    if fresh_orange==0:
        return time
    else:
        print(fresh_orange)
        return -1
grid=[[2,1,1],[0,1,1],[1,0,1]]
print(rotten_orange(grid))