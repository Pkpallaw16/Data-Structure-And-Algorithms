def sorting(l):
    lo=0
    hi=len(l)-1
    while lo<hi:
        if l[lo]==0:
            lo+=1
        else:
            l[lo],l[hi]=0,1
            hi-=1

def sort_zero_one(l):
    i=0 #points to first unsorted
    j=0 #points to first one
    while i<len(l):
        if l[i]==1:
            i+=1
        else:
            l[i],l[j]=l[j],l[i]
            i+=1
            j+=1
l=[0,1,0,1,0,0]
sorting(l)
print(l)
sort_zero_one(l)
print(l)