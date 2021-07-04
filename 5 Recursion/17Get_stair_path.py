"""1. You are given a number n representing number of stairs in a staircase.
2. You are standing at the bottom of staircase. You are allowed to climb 1 step, 2 steps or 3 steps in one move.
3. Complete the body of getStairPaths function - without changing signature - to get the list of all paths that can be used to climb the staircase up.
Use sample input and output to take idea about output."""
def get_stair_path(n):
    if n==0:
        bres=[]
        bres.append("")
        return bres
    elif n<0:
        bres=[]
        return bres
    path1=get_stair_path(n-1)
    path2=get_stair_path(n-2)
    path3=get_stair_path(n-3)
    paths=[]
    for path in path1:
        paths.append("1"+path)
    for path in path2:
        paths.append("2"+path)
    for path in path3:
        paths.append("3"+path)
    return paths
def get_stair_path_smartcall(n):
    if n==0:
        bres=[]
        bres.append("")
        return bres
    paths = []
    if n-1>=0:
        path1=get_stair_path_smartcall(n-1)
        for path in path1:
            paths.append("1" + path)
    if n - 2 >= 0:
        path2=get_stair_path_smartcall(n-2)
        for path in path2:
            paths.append("2" + path)
    if n - 3 >= 0:
        path3 = get_stair_path_smartcall(n - 3)
        for path in path3:
            paths.append("3" + path)

    return paths
def get_stair_path_smartcall_2nd_method(n):
    if n==0:
        bres=[]
        bres.append("")
        return bres
    paths = []
    for jump in range(1,4):
        if n-jump>=0:
            res=get_stair_path_smartcall_2nd_method(n-jump)
            for path in res:
                paths.append(str(jump)+path)
    return paths
n=int(input("enter number of stairs"))
print(get_stair_path(n))
print(get_stair_path_smartcall(n))
print(get_stair_path_smartcall_2nd_method(n))