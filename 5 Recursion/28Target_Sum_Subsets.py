
def target_Sum_Subsets(arr,idx,a,sos,tar):
    if idx==len(arr):
        if sos==tar:
            print(a)
        return
    if sos+arr[idx]<=tar:
        target_Sum_Subsets(arr,idx+1,a+[arr[idx]],sos+arr[idx],tar)

    target_Sum_Subsets(arr, idx + 1, a, sos, tar)
n=int(input("Enter size of list: "))
lis=[]
for i in range(n):
    lis.append(int(input()))
tar=int(input())
print(target_Sum_Subsets(lis,0,[],0,tar))


