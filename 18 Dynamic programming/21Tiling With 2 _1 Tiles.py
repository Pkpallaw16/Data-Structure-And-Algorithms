def Tiling_With_Tiles(n):
    if n==2 or n==1:
        return n
    count=0
    count+=Tiling_With_Tiles(n-1)
    count+=Tiling_With_Tiles(n-2)
    return count
def Tiling_With_Tiles_recursive(n,dp):
    if n==2 or n==1:
        dp[n]=n
        return dp[n]
    if dp[n]!=0:
        return dp[n]
    count=0
    count+=Tiling_With_Tiles_recursive(n-1,dp)
    count+=Tiling_With_Tiles_recursive(n-2,dp)
    dp[n]=count
    return dp[n]
def Tiling_With_Tiles_tab(n):
    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
def Tiling_With_Tiles_tab1(n):
    a=1
    b=2
    for i in range(1,n):
        c=a+b
        a=b
        b=c
    return a
n=5
print(Tiling_With_Tiles(n))
print(Tiling_With_Tiles_tab(n))
dp=[0 for i in range(n+1)]
print(Tiling_With_Tiles_recursive(n,dp))