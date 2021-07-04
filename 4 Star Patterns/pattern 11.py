n=int(input("enter number"))
var=1
for r in range(1,n+1):
    for c in range(1,r+1):
        print(var,end="  ")
        var+=1
    print()