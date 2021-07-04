def Unbounded_Knapsack(wts,val,indx,cap):
    if cap==0 or indx==-1:
        return 0
    v1=0
    if cap-wts[indx]>=0:
        v1=Unbounded_Knapsack(wts, val, indx, cap-wts[indx])+val[indx]
    v2=Unbounded_Knapsack(wts,val,indx-1,cap)
    return max(v1,v2)
def Unbounded_Knapsack_memoisation(wts,val,indx,cap,dp):
    if cap==0 or indx==-1:
        dp[indx+1][cap]=0
        return dp[indx+1][cap]
    if dp[indx+1][cap]!=0:
        return dp[indx+1][cap]
    v1=0
    if cap-wts[indx]>=0:
        v1=Unbounded_Knapsack(wts, val, indx, cap-wts[indx])+val[indx]
    v2=Unbounded_Knapsack(wts,val,indx-1,cap)
    dp[indx + 1][cap]=max(v1,v2)
    return dp[indx+1][cap]
def unbounded_knapsack_tab(weight,value,cap):
    dp=[0 for i in range(cap+1)]
    for indx in range(len(weight)):
        for c in range(cap+1):
            v1=dp[c]
            v2=dp[c-weight[indx]]+value[indx]
            dp[c]=max(v1,v2)
    print(dp[cap])

n=int(input("Enter size of vals : "))
vals=[int(x) for x in input().split()]
wts=[int(x) for x in input().split()]
cap=int(input("Enter capacity : "))
Unbounded_Knapsack(wts,vals,n-1,cap)