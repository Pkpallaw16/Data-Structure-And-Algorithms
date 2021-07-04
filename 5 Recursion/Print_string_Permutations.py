def print_string_permutation(ques,asf):
    if len(ques)==0:
        print(asf)
        return
    for i in range(len(ques)):
        ch=ques[i]
        rques=ques[:i]+ques[i+1:]
        print_string_permutation(rques,asf+ch)

str=input("enter string")
print_string_permutation(str,"")


