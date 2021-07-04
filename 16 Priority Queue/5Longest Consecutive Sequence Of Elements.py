def Longest_Consecutive_Sequence_Of_Elements(arr):
    freq={}
    for ele in arr:
        if ele-1 in arr:
            freq[ele]=True
        else:
            freq[ele]=False
    max_count=-1
    max_key=None
    for key in freq.keys():
        c=key
        count=0
        if freq[c]==False:
            c+=1
            while c in freq:
                c+=1
                count+=1
            if count>max_count:
                max_count=count
                max_key=key
    for i in range(max_count+1):
        print(max_key+i)

def Longest_Consecutive_Sequence_Of_Elements_2nd(arr):
     ans=0
     max_ele=None
     for ele in arr:
         if ele-1 not in arr:
             j=ele
             while j in arr:
                 j+=1
             if ans<j-ele:
                 ans=j-ele
                 max_ele=ele
     for i in range(ans):
         print(max_ele + i)
def Longest_Consecutive_Sequence_Of_Elements_3rd(arr):
    freq={}
    for ele in arr:
        freq[ele]=True
    for key in arr:
        if key-1 in freq:
            freq[key]=False
        max_len=0
        starting=0
        for key in arr:
            if freq[key]==True:
                len=1
                st=key
                while key+1 in freq:
                    len+=1
                    key+=1
                if max_len<len:
                    max_len=len
                    starting=st
                freq[st]=False
        for i in range(max_len):
            print(starting+i)
Longest_Consecutive_Sequence_Of_Elements_2nd([17,12,5,1,2,10,2,13,7,11,8,9,11,8,9,5,6,11])
print()
Longest_Consecutive_Sequence_Of_Elements([17,12,5,1,2,10,2,13,7,11,8,9,11,8,9,5,6,11])
print()
Longest_Consecutive_Sequence_Of_Elements_3rd([17,12,5,1,2,10,2,13,7,11,8,9,11,8,9,5,6,11])
print()