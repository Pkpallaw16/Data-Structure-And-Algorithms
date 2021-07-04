def str_diff_consecutive_char(str1):
    ans=str1[0]
    for i in range(1,len(str1)):
        diff=ord(str1[i])-ord(str1[i-1])
        ans=ans+str(diff)
        ans=ans+str1[i]
    return ans
str1=input("enter string")
print(str_diff_consecutive_char(str1))