def Get_Common_Elements(arr1,arr2):
    freq={}
    for ele in arr1:
        if ele in freq:
            freq[ele]+=1
        else:
            freq[ele]=1
    for key in arr2:
        if key in freq:
            print(key)
            del freq[key]

def Get_Common_Elements_2nd(arr1,arr2):
    freq={}
    for ele in arr2:
        if ele not in freq and ele in arr1:
            print(ele)
            freq[ele] = 1

Get_Common_Elements([5,5,9,8,5,5,8,0,3],[9,7,1,0,3,6,5,9,1,1,8,0,2,4,2,9,1,5])
print()
Get_Common_Elements_2nd([5,5,9,8,5,5,8,0,3],[9,7,1,0,3,6,5,9,1,1,8,0,2,4,2,9,1,5])
