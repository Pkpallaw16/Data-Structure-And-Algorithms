n=int(input("enter num "))
for i in range(0,n):
    val=1
    for j in range(0,i+1):
        print(val,end=" ")
        val=int((val*(i-j))/(j+1))
    print()