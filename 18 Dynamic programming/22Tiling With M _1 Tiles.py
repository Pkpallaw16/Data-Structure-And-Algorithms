def Tiling_With_Tiles(n,m):
    if n==1:
        return 1
    if n==m:
        return 2
    count=0
    count+=Tiling_With_Tiles(n-1,m)
    if n-m>=0:
        count+=Tiling_With_Tiles(n-m,m)
    return count

def Tiling_With_Tiles_recursive(n,m,dp):
    if n==1:
        dp[n]=1
        return dp[n]
    if n==m:
        dp[n]=2
        return dp[n]
    count=0
    count+=Tiling_With_Tiles_recursive(n-1,m,dp)
    if n-m>=0:
        count+=Tiling_With_Tiles_recursive(n-m,m,dp)
    dp[n]= count
    return dp[n]
def Tiling_With_Tiles_tab(n,m):
    dp=[0 for i in range(n+1)]
    for i in range(n+1):
        if i<m:
            dp[i]=1
        else:
            dp[i]=dp[i-1]+dp[i-m]
    return dp[n]
n=39
dp=[0 for i in range(n+1)]
print(Tiling_With_Tiles(39,16))
print(Tiling_With_Tiles_recursive(n,16,dp))
print(Tiling_With_Tiles_tab(n,16))
