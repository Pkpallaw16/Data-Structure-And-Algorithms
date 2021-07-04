
def target_Sum_Subsets(arr,idx,a,sos,tar,count):
    if idx==len(arr):
        if count==2 and sos==tar:
            print(a)
        return
    if sos+arr[idx]<=tar:
        target_Sum_Subsets(arr,idx+1,a+[arr[idx]],sos+arr[idx],tar,count+1)

    target_Sum_Subsets(arr, idx + 1, a, sos, tar,count)




def target_sum_parir(arr,tar):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        sum=arr[left]+arr[right]
        if sum==tar:
            print(arr[left],arr[right])
            left+=1
            right-=1
        elif sum>tar:
            right-=1
        else:
            left+=1
arr=[10,30,40,20,50,60,15,35]
target_Sum_Subsets(arr,0,[],0,70,0)
target_sum_parir(arr,70)