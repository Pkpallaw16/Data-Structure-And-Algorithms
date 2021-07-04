def climb_stairs_with_variable_jump(dp,n,last_stair,jump):
    if n==last_stair:
        dp[n] = 1
        return dp[n]
    if dp[n]!=0:
        return dp[n]
    path_count=0
    for i in range(1,jump[n]+1):
        if n+i<=last_stair:
            path_count += climb_stairs_with_variable_jump(dp, n + i,last_stair,jump)
    dp[n] = path_count
    return dp[n]
def climb_stairs_with_variable_jump_tabulation(dp,n,jump):
    for i in range(n,-1,-1):
        if i==n:
            dp[n]=1
            continue
        path_count=0
        for step in range(1,jump[i]+1):
            if i+step<=n:
                path_count+=dp[i+step]
        dp[i]=path_count
    return dp[0]
n=int(input("enter number of stairs"))
dp=[0 for i in range(n+1)]
jump=[]
for i in range(n):
    jump.append(int(input()))
print(climb_stairs_with_variable_jump(dp,0,n,jump))
print(climb_stairs_with_variable_jump_tabulation(dp,n,jump))