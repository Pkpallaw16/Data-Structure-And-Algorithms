def maximum_amount_of_gold_recursion(goldmine,r,c):
    if c==len(goldmine[0])-1:
        return goldmine[r][c]
    maxgold=0
    if r-1>=0 :
        maxgold=max(maxgold,maximum_amount_of_gold_recursion(goldmine,r-1,c+1))

    maxgold = max(maxgold, maximum_amount_of_gold_recursion(goldmine,r,c+1))
    if r + 1 < len(goldmine):
        maxgold = max(maxgold, maximum_amount_of_gold_recursion(goldmine,r+1,c+1))

    return maxgold+goldmine[r][c]
def maximum_amount_of_gold_memoization(dp,goldmine,r,c):
    if c == len(goldmine[0]) - 1:
        dp[r][c]=goldmine[r][c]
        return dp[r][c]
    if dp[r][c]!=0:
        return dp[r][c]
    maxgold = 0
    if r - 1 >= 0:
        maxgold = max(maxgold, maximum_amount_of_gold_memoization(dp,goldmine, r - 1, c + 1))

    maxgold = max(maxgold, maximum_amount_of_gold_memoization(dp,goldmine, r, c + 1))
    if r + 1 < len(goldmine):
        maxgold = max(maxgold, maximum_amount_of_gold_memoization(dp,goldmine, r + 1, c + 1))
    dp[r][c]=maxgold + goldmine[r][c]
    return dp[r][c]
def maximum_amount_of_gold_tabulation(goldmine,dp):
    for j in range(len(goldmine[0])-1,-1,-1):
        for i in range(len(goldmine)):
            if j ==len(goldmine[0])-1:
                dp[i][j]=goldmine[i][j]
                continue
            elif i==0:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j+1])+goldmine[i][j]
            elif i==len(goldmine)-1:
                dp[i][j] = max(dp[i][j + 1], dp[i - 1][j + 1]) + goldmine[i][j]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j + 1],dp[i - 1][j + 1]) + goldmine[i][j]

def maximum_amount_of_gold_tab2(dp,goldmine):
    maxgold=0
    for c in range(len(goldmine[0])-1,-1,-1):
        for r in range(len(goldmine)):
            if c==len(goldmine[0])-1:
                dp[r][c]=goldmine[r][c]
                maxgold=max(maxgold,dp[r][c])
                continue
            gold = 0
            if r - 1 >= 0:
                gold = max(gold, dp[r - 1][c + 1])
            gold = max(gold, dp[r][c + 1])
            if r + 1 < len(goldmine):
                gold = max(gold, dp[r + 1][c + 1])
            dp[r][c] = gold + goldmine[r][c]
            maxgold = max(maxgold, dp[r][c])
    return maxgold
row=int(input("enter number of row: "))
col=int(input("enter number of col: "))
goldmine=[[int(x) for x in input().split()] for i in range(row)]
dp=[[0 for i in range(col)] for j in range(row)]
#Tabulation
maximum_amount_of_gold_tabulation(goldmine,dp)
print(max([x[0] for x in dp]))

maxgold=0
for r in range(len(goldmine)):
    maxgold=max(maxgold,maximum_amount_of_gold_recursion(goldmine,r,0))
print(maxgold)
maxgold_memoization=0
#Memoization
dp=[[0 for i in range(col)] for j in range(row)]
for r in range(len(goldmine)):
    maxgold_memoization=max(maxgold_memoization,maximum_amount_of_gold_memoization(dp,goldmine,r,0))
print(maxgold_memoization)
dp=[[0 for i in range(col)] for j in range(row)]
print(maximum_amount_of_gold_tab2(dp,goldmine))
