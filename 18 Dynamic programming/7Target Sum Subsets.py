def Target_Sum_Subsets(lis,tar,ind):
    if tar==0:
        return True
    if ind==len(lis):
        return False
    res=False
    if tar-lis[ind]>=0:
        res=Target_Sum_Subsets(lis, tar-lis[ind], ind + 1)
    res=res or Target_Sum_Subsets(lis,tar,ind+1)
    return res
def Target_Sum_Subsets2(lis,tar,ind,sum,a):
    if sum==tar:
        print(a)
        return
    if ind+1 <=len(lis):
        Target_Sum_Subsets(lis,tar,ind+1,sum+lis[ind],a+[lis[ind]])
        Target_Sum_Subsets(lis,tar,ind+1,sum,a)
def Target_Sum_Subsets_memoization(lis,tar,ind,dp):
    if tar==0:
        dp[ind][tar]=True
        return dp[ind][tar]
    if ind==len(lis):
        dp[ind][tar] = False
        return dp[ind][tar]
    if dp[ind][tar]!=None:
        return dp[ind][tar]
    res=False
    if tar-lis[ind]>=0:
        res=Target_Sum_Subsets(lis, tar-lis[ind], ind + 1)
    res=res or Target_Sum_Subsets(lis,tar,ind+1)
    dp[ind][tar]=res
    return dp[ind][tar]
def Target_Sum_Subsets_Tabulation(arr,target):
    dp = [[None for i in range(target + 1)] for j in range(len(arr) + 1)]
    for indx in range(len(dp)):
        for tar in range(len(dp[0])):
            if tar==0:
                dp[indx][tar]=True
            elif indx==0:
                dp[indx][tar] = False
            else:
                val=arr[indx-1]
                if tar<val:
                    dp[indx][tar]=dp[indx-1][tar]
                else:
                    dp[indx][tar]=dp[indx-1][tar] or dp[indx-1][tar-val]
    return dp[len(dp)-1][len(dp[0])-1]
def Target_Sum_Subsets_tab2(lis,target):
    dp = [[None for i in range(target + 1)] for j in range(len(lis) + 1)]
    for indx in range(len(dp)-1,-1,-1):
        for tar in range(len(dp[0])):
            if tar == 0:
                dp[indx][tar] = True
                continue
            if indx == len(lis):
                dp[indx][tar] = False
                continue
            res=False

            if tar-lis[indx]>=0:
                res=dp[indx + 1][tar-lis[indx]]
            res=res or dp[indx + 1][tar]
            dp[indx][tar]=res
    return dp[0][tar]
n=int(input("Enter size of list: "))
lis=[]
for i in range(n):
    lis.append(int(input()))
tar=int(input())
print(Target_Sum_Subsets(lis,tar,0))
dp=[[None for i in range(tar+1)] for j in range(n+1)]
print(Target_Sum_Subsets_memoization(lis,tar,0,dp))
print(Target_Sum_Subsets_Tabulation(lis,tar))