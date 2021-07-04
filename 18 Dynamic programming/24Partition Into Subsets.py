def Partition_Into_Subsets(n,k):
    dp=[[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(n+1):
        for j in range(i+1):
            if j<=k:
                if j==0:
                    dp[i][j]=0
                elif i==j:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j-1]+(j*dp[i-1][j])
    return dp[n][k]           