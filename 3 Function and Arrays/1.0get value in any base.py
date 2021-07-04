def get_value_any_base(n,b):
    ans=0
    pow=0
    while n>0:
        rem=n%b
        quo=n/b
        ans=ans+(pow*rem)
        pow=pow*10
        n=quo
    return ans

n=int(input("enter number"))
b=int(input("enter base"))
get_value_any_base(n,b)