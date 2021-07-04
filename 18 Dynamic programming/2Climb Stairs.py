def climb_stairs_recursion(n):
    if n==0:
        return 1
    count=0
    for step in range(1,4):
        if n-step>=0:
            count+=climb_stairs_recursion(n-step)

    return count
def climb_stairs_memoization(dp,n,last_stair):
    if n>last_stair:
        return 0
    if n==last_stair:
        return 1
    if dp[n]!=0:
        return dp[n]
    path1 = climb_stairs_memoization(dp, n + 1,last_stair)
    path2 = climb_stairs_memoization(dp, n + 2,last_stair)
    path3 = climb_stairs_memoization(dp, n + 3,last_stair)
    path = path1 + path2 + path3
    dp[n] = path
    return path
def climb_stairs_tabulation(dp,n):
    dp[0]=1
    for i in range(1,n+1):
        count=0
        for step in range(1,4):
            if i-step>=0:
                count+=dp[i-step]
        dp[i]=count
    return dp[n]
n=int(input("enter number of stairs"))
dp=[0 for i in range(n+1)]
print(climb_stairs_memoization(dp,0,n))
print(climb_stairs_recursion(n))
print(climb_stairs_tabulation(dp,n))
