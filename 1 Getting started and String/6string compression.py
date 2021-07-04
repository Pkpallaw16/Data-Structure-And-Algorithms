def str_compression(str1):
    ans=str1[0]
    count=1
    for i in range(1,len(str1)):
        if str1[i]!=str1[i-1]:

            if count>1:
                ans=ans+str(count)
            ans=ans+str1[i]
            count = 1
        else:
            count+=1
    if count>1:
        ans=ans+str(count)
    return ans
str1=input("enter string")
print(str_compression(str1))