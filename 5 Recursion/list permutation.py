#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

def list_permutation(list,lsf,permuation):
    if list==[]:
        if lsf not in permutaion:
            permuation.append(lsf)
    for i in range(len(list)):
        item=list[i]
        rlist=list[:i]+list[i+1:]
        list_permutation(rlist,lsf+[item],permuation)

permutaion=[]
list_permutation([1,1,3],[],permutaion)
print(permutaion)
