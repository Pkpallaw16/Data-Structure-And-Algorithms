def Min_Cost_In_Maze_Traversal(maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        return maze[r][c]
    mincost=int(1e9)
    if c+1<len(maze[0]):
        mincost=min(mincost,Min_Cost_In_Maze_Traversal(maze,r,c+1))
    if r+1<len((maze)):
        mincost = min(mincost, Min_Cost_In_Maze_Traversal(maze,r+1,c))
    return mincost+maze[r][c]
def Min_Cost_In_Maze_Traversal_memoization(dp,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        dp[r][c]=maze[r][c]
        return dp[r][c]
    if dp[r][c]!=0:
        return dp[r][r]
    mincost=int(1e9)
    if c+1<len(maze[0]):
        mincost=min(mincost,Min_Cost_In_Maze_Traversal(maze,r,c+1))
    if r+1<len((maze)):
        mincost = min(mincost, Min_Cost_In_Maze_Traversal(maze,r+1,c))
    dp[r][c]=mincost+maze[r][c]
    return dp[r][c]
def Min_Cost_In_Maze_Traversal_tabulation(maze,dp):
    for i in range(len(maze)-1,-1,-1):
        for j in range(len(maze[0])-1,-1,-1):
            if i==len(maze)-1 and j==len(maze[0])-1:
                dp[i][j]=maze[i][j]
            elif i==len(maze)-1:
                dp[i][j]=dp[i][j+1]+maze[i][j]
            elif j==len(maze[0])-1:
                dp[i][j]=dp[i+1][j]+maze[i][j]
            else:
                dp[i][j]=min(dp[i][j+1],dp[i+1][j])+maze[i][j]
    return dp[0][0]
def Min_Cost_In_Maze_Traversal_tabulation2(maze,dp):
    for i in range(len(maze)-1,-1,-1):
        for j in range(len(maze[0])-1,-1,-1):
            if i==len(maze)-1 and j==len(maze[0])-1:
                dp[i][j]=maze[i][j]
                continue
            mincost=int(1e9)
            if i+1<len(maze):
                mincost=min(mincost,dp[i+1][j])
            if j+1<len(maze[0]):
                mincost=min(mincost,dp[i][j+1])
            dp[i][j]=mincost+maze[i][j]
    return dp[0][0]
def min_mazepath(dp,x,y,psf):
    if x==len(dp)-1 and y==len(dp[0])-1:
        print(psf)
    elif x==len(dp)-1:
        min_mazepath(dp,x,y+1,psf+"R")
    elif y==len(dp[0])-1:
        min_mazepath(dp, x+1, y, psf +"D")
    else:
        if dp[x][y+1]==dp[x+1][y]:
            min_mazepath(dp, x + 1, y, psf + "D")
            min_mazepath(dp, x, y + 1, psf + "R")
        elif dp[x][y+1]<dp[x+1][y]:
            min_mazepath(dp, x, y + 1, psf + "R")
        else:
            min_mazepath(dp, x + 1, y, psf + "D")


r=int(input("enter number of row: "))
c=int(input("enter number of col: "))
maze=[[int(x) for x in input().split()] for i in range(r)]
dp=[[0 for i in range(c)] for j in range(r)]
print(Min_Cost_In_Maze_Traversal(maze,0,0))
print(Min_Cost_In_Maze_Traversal_memoization(dp,maze,0,0))
print(Min_Cost_In_Maze_Traversal_tabulation(maze,dp))
print(dp)
dp=[[0 for i in range(c)] for j in range(r)]
print(Min_Cost_In_Maze_Traversal_tabulation2(maze,dp))
print(dp)
min_mazepath(dp,0,0,"")