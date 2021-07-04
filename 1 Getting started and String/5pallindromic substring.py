def is_pallindrom(str1):
    i=0
    j=len(str1)-1
    while i<j:
        if str1[i]!=str1[j]:
            return False
        i+=1
        j-=1
    return True
def pallindromic_subsstring(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
            temp=str[i:j]
            if is_pallindrom(temp):
                print(temp)


str=input("enter string")
pallindromic_subsstring(str)