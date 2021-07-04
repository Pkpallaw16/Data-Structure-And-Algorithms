def fibmemoized_recursion(n):
    if n==0 or n==1:
        return n
    fibn1=fibmemoized_recursion(n-1)
    fibn2=fibmemoized_recursion(n-2)
    fibn=fibn1 + fibn2
    return fibn
#memoization
def fibmemoized_memoization(storage,n):

    if n==0 or n==1:
        return n
    if storage[n]!=0:
        return storage[n]

    fibn1=fibmemoized_memoization(storage,n-1)
    fibn2=fibmemoized_memoization(storage,n-2)
    fibn=fibn1 + fibn2
    storage[n]=fibn
    return fibn
def fibmemoized_tabulation(storage_tabulation,n):
    #figure out repitition
    #make a storage of size n+1
    storage_tabulation[0]=0
    storage_tabulation[1]=1
    for i in range(2,n+1):
        storage_tabulation[i]=storage_tabulation[i-1]+storage_tabulation[i-2]
    return storage_tabulation[n]



n = int(input("enter number"))
storage_memoization=[0 for i in range(n+1)]
print(fibmemoized_memoization(storage_memoization,n))
storage_tabulation=[0 for i in range(n+1)]
print(fibmemoized_tabulation(storage_tabulation,n))
