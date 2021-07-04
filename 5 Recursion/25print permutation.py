def print_Permutations(s,asf):
    if s=="":
        print(asf)
    new_lis=[]
    for i in range(len(s)):
        ch=s[i:i+1]
        s1=s[:i]+s[i+1:]
        lis=print_Permutations(s1,asf+ch)


print_Permutations("abc","")

