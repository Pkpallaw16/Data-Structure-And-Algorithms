import sys
def climb_stairs_with_minimum_moves_recursion(n,last_stair,jump):
    if n==last_stair:
        return 0
    min_moves=int(1e9)
    for i in range(1,jump[n]+1):
        if n+i<=last_stair:
            moves=climb_stairs_with_minimum_moves_memoization(n + i,last_stair,jump)
            min_moves= min(moves,min_moves)
    if min_moves!=int(1e9):
        min_moves= min_moves+1
    return min_moves
def climb_stairs_with_minimum_moves_memoization(dp,n,last_stair,jump):
    if n==last_stair:
        dp[n] = 0
        return dp[n]
    if dp[n]!=0:
        return dp[n]
    min_moves=int(1e9)
    for i in range(1,jump[n]+1):
        if n+i<=last_stair:
            moves=climb_stairs_with_minimum_moves_memoization(dp, n + i,last_stair,jump)
            min_moves= min(moves,min_moves)
    if min_moves!=sys.maxsize:
        dp[n] = min_moves+1
    else:
        dp[n]=min_moves
    return dp[n]
def climb_stairs_with_minimum_moves_tabulation(dp,n,jump):
    for i in range(n,-1,-1):
        if i==n:
            dp[n]=0
            continue
        min_moves=int(1e9)
        for step in range(1,jump[i]+1):
            if i+step<=n and dp[i+step]!=-1:
                min_moves=min(min_moves,dp[i+step])
        if min_moves!=int(1e9):
            dp[i]=min_moves+1
        else:
            dp[i]=min_moves
    return dp[0]
def climb_stairs_with_minimum_moves_tabulation2(dp,n,jump):
    dp[n] = 0
    for i in range(n-1,-1,-1):
        min_moves=int(1e9)
        for step in range(1,jump[i]+1):
            if i+step<=n and dp[i+step]!=-1:
                min_moves=min(min_moves,dp[i+step])
        if min_moves!=int(1e9):
            dp[i]=min_moves+1
        else:
            dp[i]=min_moves
    return dp[0]
n=int(input("enter number of stairs"))
dp1=[-1 for i in range(n+1)]
dp2=[-1 for i in range(n+1)]
jump=[]
for i in range(n):
    jump.append(int(input()))
res=climb_stairs_with_minimum_moves_memoization(dp1,0,n,jump)
if res==int(1e9):
    print("None")
else:
    print(res)
res=climb_stairs_with_minimum_moves_tabulation(dp2,n,jump)
if res==int(1e9):
    print("None")
else:
    print(res)
print(dp1)
print(jump)
print(dp2)