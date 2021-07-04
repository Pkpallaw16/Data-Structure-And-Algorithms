def Maximum_Sum_Non_Adjacent_Elements(lis,indx):
    if indx<0:
        return 0
    v1=Maximum_Sum_Non_Adjacent_Elements(lis,indx-2)+lis[indx]
    v2=Maximum_Sum_Non_Adjacent_Elements(lis,indx-1)
    return max(v1,v2)
def Maximum_Sum_Non_Adjacent_Elements_recursion(lis,indx,last_call):
    if indx==-1:
        return 0
    maxsum=-int(1e9)
    if last_call==0:
        maxsum=Maximum_Sum_Non_Adjacent_Elements_recursion(lis,indx-1,1)+lis[indx]
    maxsum=max(maxsum,Maximum_Sum_Non_Adjacent_Elements_recursion(lis,indx-1,0))
    return maxsum
def Maximum_Sum_Non_Adjacent_Elements_memoisation(lis,indx,last_call,dp):
    if indx==-1:
        dp[last_call][indx+1]=0
        return 0
    if dp[last_call][indx+1]!=0:
        return dp[last_call][indx+1]
    maxsum=-int(1e9)
    if last_call==0:
        maxsum=Maximum_Sum_Non_Adjacent_Elements_memoisation(lis,indx-1,1,dp)+lis[indx]
    maxsum=max(maxsum,Maximum_Sum_Non_Adjacent_Elements_memoisation(lis,indx-1,0,dp))
    dp[last_call][indx+1]= maxsum
    return dp[last_call][indx+1]
def Maximum_Sum_Non_Adjacent_Elements_optimised_tab(lis):
    include=0
    exclude=0
    for i in range(len(lis)):
        new_include=exclude+lis[i]
        new_exclude=max(exclude,include)
        include=new_include
        exclude=new_exclude
    return max(include,exclude)

lis=[]
n=int(input("enter size of list "))
for i in range(n):
    lis.append(int(input()))
print(Maximum_Sum_Non_Adjacent_Elements(lis,len(lis)-1))
print(Maximum_Sum_Non_Adjacent_Elements_recursion(lis,len(lis)-1,0))
dp=[[0 for i in range(n+1)] for j in range(2)]
print(Maximum_Sum_Non_Adjacent_Elements_memoisation(lis,len(lis)-1,0,dp))
print(Maximum_Sum_Non_Adjacent_Elements_optimised_tab(lis))
