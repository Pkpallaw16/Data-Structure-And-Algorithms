def segregate_odd_even(l):
    i = 0  # points to first unsorted
    j = 0  # points to first even
    while i < len(l):
        if l[i]%2==0:
            i += 1
        else:
            l[i], l[j] = l[j], l[i]
            i += 1
            j += 1


list=[4,6,7,5,2,3,1,8,4]
segregate_odd_even(list)
print(list)