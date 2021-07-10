def coin_change_combination_recursion(coins,target,indx,psf):
    if target==0:
        print(psf)
        return 1
    count=0
    if indx==len(coins):
        return 0
    if target-coins[indx]>=0:
        count+=coin_change_combination_recursion(coins,target-coins[indx],indx,psf+str(coins[indx]))
    count += coin_change_combination_recursion(coins, target, indx+1, psf)
    return count
def coin_change_combination_memoization(coins,target,indx,psf,dp):
    if target==0:
        print(psf)
        dp[target]=1
        return dp[target]
    if indx==len(coins):
        dp[target]=0
        return dp[target]
    if dp[target]!=0:
        return dp[target]
    count=0

    if target-coins[indx]>=0:
        count+=coin_change_combination_memoization(coins,target-coins[indx],indx,psf+str(coins[indx]),dp)
    count += coin_change_combination_memoization(coins, target, indx+1, psf,dp)
    dp[target]= count
    return dp[target]
def coin_change_combination_tabulation(coins,target):
    dp=[0 for i in range(target+1)]
    dp[0]=1
    for coin in coins:
        for tar in range(coin,target+1):
            if tar-coin>=0:
                dp[tar]+=dp[tar-coin]
    return dp[target]
def coin_change_combination_tab2(coins,target,dp):
    for indx in range(len(coins),-1,-1):
        for tar in range(target+1):
            if tar==0:
                dp[indx][tar]=1
                continue
            if indx==len(coins):
                dp[indx][tar]=0
                continue
            count=0
            if tar-coins[indx]>=0:
                count+=dp[indx][tar-coins[indx]]
            count+=dp[indx+1][tar]
            dp[indx][tar]=count
    return dp[0][target]
coins=[2,3,5,6]
target=7
dp=[0 for i in range(target+1)]
print(coin_change_combination_recursion(coins,target,0,""))
dp=[0 for i in range(target+1)]
print(coin_change_combination_memoization(coins,target,0,"",dp))
print(coin_change_combination_tabulation(coins,target))
dp=[[0 for i in range(target+1)] for j in range(len(coins)+1)]
print(coin_change_combination_tab2(coins,target,dp))