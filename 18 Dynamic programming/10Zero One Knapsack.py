import numpy as np
def Zero_one_knapsack_recursive(wts,vals,indx,cap):
    if indx==-1:
        return 0
    #yes call
    v1=0
    if cap-wts[indx]>=0:
        v1=Zero_one_knapsack_recursive(wts,vals,indx-1,cap-wts[indx]) +vals[indx]
    # no call
    v2=Zero_one_knapsack_recursive(wts,vals,indx-1,cap)

    return max(v1,v2)
def Zero_one_knapsack_recursive_memoization(wts,vals,indx,cap,dp):
    if indx==-1:
        dp[indx+1][cap]==0
        return dp[indx+1][cap]
    if dp[indx+1][cap]!=0:
        return dp[indx+1][cap]
    #yes call
    v1=0
    if cap-wts[indx]>=0:
        v1=Zero_one_knapsack_recursive_memoization(wts,vals,indx-1,cap-wts[indx],dp) +vals[indx]
    # no call
    v2=Zero_one_knapsack_recursive_memoization(wts,vals,indx-1,cap,dp)
    dp[indx + 1][cap]=max(v1,v2)
    return dp[indx + 1][cap]

def zero_one_knapsack(wts,vals,capacity,dp):
    for indx in range(1,len(vals)+1):
        for cap in range(1,capacity+1):
            if cap<wts[indx-1]:
                dp[indx][cap]=dp[indx-1][cap]
            else:
                #yes call
                v1=dp[indx-1][cap-wts[indx-1]]+vals[indx-1]
                #no call
                v2=dp[indx-1][cap]
                dp[indx][cap]=max(v1,v2)
    print(dp[len(wts)][cap])
n=int(input("Enter size of vals : "))
vals=[int(x) for x in input().split()]
wts=[int(x) for x in input().split()]
cap=int(input("Enter capacity : "))
Zero_one_knapsack_recursive(wts,vals,n-1,cap)