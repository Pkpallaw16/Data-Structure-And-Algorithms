def sort_zero_one(l):
    i=0 #points to first unsorted
    j=0 #points to first one
    k=len(l)-1
    while i<=k:
        if l[i]==1:
            i+=1
        elif l[i]==0:
            l[i],l[j]=l[j],l[i]
            i+=1
            j+=1
        else:
            l[i],l[k]=l[k],l[i]
            k-=1

def sort_zero_one_2nd(l):
    i = 0  # points to first unsorted
    j = 0  # points to first even
    k=0
    while i < len(l):
        if l[i]==0:
            l[i], l[j] = l[j], l[i]
            l[i], l[k] = l[k], l[i]
            i += 1
            j+=1
            k+=1
        elif l[i]==1:
            l[i], l[k] = l[k], l[i]
            i += 1
            k += 1
        else:
            i+=1
list=[1,0,2,2,1,0,2,1,0,2]
list1=[1,0,2,2,1,0,2,1,0,2]
sort_zero_one(list)
print(list)
sort_zero_one_2nd(list1)
print(list1)