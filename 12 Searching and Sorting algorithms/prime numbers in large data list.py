import math
def bSearch(l, lo,hi,data):
    #O(logn)
    if lo>hi:
        return -1
    mid = (lo + hi) // 2
    if l[mid] == data:
        return mid
    elif l[mid] < data:
        return bSearch(l, mid + 1, hi, data)
    else:
        return bSearch(l, lo, mid - 1, data)

n=int(input("enter first num "))
list=[]
for i in range(n):
    list.append(int(input()))
flag=0
numbers=[]
for i in range(41):
    for div in range(2,int(math.sqrt(i))+1):
        if i%div==0:
            flag=1
            break
    if flag==0:
        numbers.append(i)
    flag=0
for i in range(len(list)):
    index=bSearch(numbers,list[i])
    if index!=-1:
        print(list[index])