def stair_path_with_jumps(n,jumps,os):
    if n==0:
        return [""]
    mres=[]
    for step in range(1,jumps[n]+1):
        if n-step>=0:
            res=stair_path_with_jumps(n-step,jumps)
            for path in res:
                mres.append(str(step)+path)
    if n==os and len(mres)==0:
        print("no possible path")
    return mres
jumps=[1,0,2,1,4,0,2,3]
print(stair_path_with_jumps(7,jumps,7))