def print_encoding(ques,asf):
    if len(ques)==0:
        print(asf)
        return
    elif len(ques)==1:
        c=ques[0]
        if c=='0':
            return
        else:
            ch=chr(ord('a')+int(c)-1)
            print(asf+ch)
    else:
        ch1=ques[0]
        rques=ques[1:]
        if ch1=='0':
            return
        else:
            ch = chr(ord('a') + int(ch1) - 1)
            print_encoding(rques,asf + ch)

        ch12 = ques[0:2]
        rques12 = ques[2:]
        if int(ch12)<=26:
            ch = chr(ord('a') + int(ch12) - 1)
            print_encoding(rques12, asf + ch)

str=input("enter string")
print_encoding(str,"")
