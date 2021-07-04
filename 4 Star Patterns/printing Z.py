n=6
for i in range(n):
    print("*",end="")
print()
for j in range(n-1,1,-1):
    for i in range(j):
        if i==j-1:
            print("*")
            break
        print(end=" ")
for i in range(n):
    print("*",end="")
