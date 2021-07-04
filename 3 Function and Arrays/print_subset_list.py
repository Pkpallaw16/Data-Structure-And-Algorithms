import math
def decimal_to_bin(n):
    pow=1
    bin=0
    while n>0:
        rem=n%2
        n=int(n/2)
        bin=bin+rem*pow
        pow=pow*10
    return bin

def subset_list(lis):
    l = int(math.pow(2, len(lis)))
    for i in range(l):
        binary=decimal_to_bin(i)
        subset=""
        for j in range(len(lis)-1,-1,-1):
            digit=binary%10
            binary=int(binary/10)
            if digit==0:
                subset="- "+subset
            else:
                subset=str(lis[j])+" "+subset
        print(subset)

lis=[1,2,3,4,5]
subset_list(lis)
