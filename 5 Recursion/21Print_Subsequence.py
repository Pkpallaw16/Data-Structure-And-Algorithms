def Print_Subsequence(str,asf):
    if len(str)==0:
        print(asf)
        return
    ch=str[0]
    rstr=str[1:]
    Print_Subsequence(rstr,asf+ch)
    Print_Subsequence(rstr,asf+"")

str=input("enter string")
Print_Subsequence(str,"")