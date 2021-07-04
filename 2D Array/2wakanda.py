m1=int(input("eneter size of array"))
m2=int(input("eneter size of array"))
arr2=[[int(input()) for i in range(m2)] for j in range(m1)]
start =0
end=0
step=1
print(arr2)
for i in range(m2):
    if i%2!=0:
        start=m1-1
        end=-1
        step=-1
    else:
        start=0
        end=m1
        step=1
    for j in range(start,end,step):
        print(arr2[j][i],end="->")
