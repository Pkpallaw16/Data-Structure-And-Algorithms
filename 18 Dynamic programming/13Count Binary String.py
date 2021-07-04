def Count_Binary_String_recursion(n,le,asf):
    if n==0:
        print(asf)
        return 1
    count=0
    if le==1:
        count+=Count_Binary_String_recursion(n-1,0,asf+"0")
    count+=Count_Binary_String_recursion(n - 1, 1, asf + "1")
    return count
def Count_Binary_String_memoisation(n,le,dp):
    if n==0:
        dp[n][le]=1
        return dp[n][le]
    if dp[n][le]!=0:
        return dp[n][le]
    count=0
    if le==1:
        count+=Count_Binary_String_memoisation(n-1,0,dp)
    count+=Count_Binary_String_memoisation(n - 1, 1,dp)
    dp[n][le]= count
    return dp[n][le]
def Count_Binary_String_tab(n):
    dp=[[0 for i in range(n)] for j in range(2)]
    dp[0][0]=1
    dp[1][0]=1
    for i in range(n):
        dp[i][0]=dp[i-1][1]
        dp[i][1]=dp[i-1][0]+dp[i-1][1]
    return dp[n-1][0]+dp[n-1][1]
def countBinaryString_optimise(n):
    zero=1
    one=1
    for i in range(2,n+1):
        n_zero=one
        n_one=one+zero
        zero=n_zero
        one=n_one
    return one+zero
print(Count_Binary_String_recursion(4,1,""))
dp=[[0 for i in range(5)] for j in range(2)]
print(Count_Binary_String_memoisation(4,1,dp))