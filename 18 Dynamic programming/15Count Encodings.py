def Count_Encodings(str,indx):
    if indx==len(str):
        return 1
    if str[indx]=='0':
        return 0
    count=0
    n1=int(str[indx])
    count+=Count_Encodings(str,indx+1)
    if indx+1<len(str):
        n=int(str[indx+1])
        n2=n1*10+n
        if n2<=26:
            count+=Count_Encodings(str,indx+2)
    return count
def Count_Encodings_memoisation(str,indx,dp):
    if indx==len(str):
        dp[indx]=1
        return dp[indx]
    if str[indx]=='0':
        dp[indx]=0
        return dp[indx]
    if dp[indx]!=0:
        return dp[indx]
    count=0
    n1=int(str[indx])
    count+=Count_Encodings(str,indx+1)
    if indx+1<len(str):
        n=int(str[indx+1])
        n2=n1*10+n
        if n2<=26:
            count+=Count_Encodings(str,indx+2)
    dp[indx]=count
    return dp[indx]

def Count_Encodings_tab1(str):
    dp=[0 for i in range(len(str)+1)]
    for indx in range(len(str),-1,-1):
        if indx==len(str):
            dp[indx]=1
            continue
        if str[indx]=='0':
            dp[indx]=0
            continue
        count=0
        n1=int(str[indx])
        count+=dp[indx+1]
        if indx+1<len(str):
            n=int(str[indx+1])
            n2=n1*10+n
            if n2<=26:
                count+=dp[indx+2]
        dp[indx]=count
    return dp[0]
print(Count_Encodings("12323",0))
dp=[0 for i in range(6)]
print(Count_Encodings_memoisation("12323",0,dp))
print(Count_Encodings_tab1("12323"))

