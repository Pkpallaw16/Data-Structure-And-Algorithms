def get_Permutations(s):
    if s=="":
        return [""]
    new_lis=[]
    for i in range(len(s)):
        char=s[i:i+1]
        s1=s[:i]+s[i+1:]
        lis=get_Permutations(s1)
        for item in lis:
            new_lis.append(item+char)

    return new_lis

print(get_Permutations("abc"))

