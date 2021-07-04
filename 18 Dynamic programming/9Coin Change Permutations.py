def coin_change_permutation(coins,target,psf):
    if target==0:
        print(psf)
        return 1
    count=0
    for coin in coins:
        if target-coin>=0:
            count+=coin_change_permutation(coins,target-coin,psf+str(coin))
    return count
def coin_change_permutation_memoisation(coins,target,dp):
    if target==0:
        dp[target]=1
        return dp[target]
    if dp[target]!=0:
        return dp[target]
    count=0
    for coin in coins:
        if target-coin>=0:
            count+=coin_change_permutation_memoisation(coins,target-coin,dp)
    dp[target] =count
    return dp[target]
def coin_change_permutation_tab1(coins,target,dp):
    dp[0]=1
    for tar in range(target+1):
        for coin in coins:
            if tar-coin>=0:
                dp[tar]+=dp[tar-coin]
    return dp[target]

coins=[2,3,5,6]
target=7
dp=[0 for i in range(target+1)]
print(coin_change_permutation(coins,target,""))
print(coin_change_permutation_memoisation(coins,target,dp))
dp=[0 for i in range(target+1)]
print(coin_change_permutation_tab1(coins,target,dp))