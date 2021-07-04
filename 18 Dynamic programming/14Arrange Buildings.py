def Arrange_Buildings(n):
    building=1
    space=1
    for i in range(2,n+1):
        n_building=space
        n_space=building+space
        space=n_space
        building=n_building
    res=building+space
    return res*res
n=int(input("enter number of building: "))
print(Arrange_Buildings(n))