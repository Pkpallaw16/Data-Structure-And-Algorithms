def Count_Abc_Subsequences(str):
    count_a=0
    count_b=0
    count_c=0
    for ch in str:
        if ch=="a":
            count_a=2*count_a+1
        elif ch=="b":
            count_b=count_a+2*count_b
        elif ch=="c":
            count_c=count_b+2*count_c
    print(count_c)
str=input("enter string ")
Count_Abc_Subsequences(str)