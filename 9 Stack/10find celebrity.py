def find_celebrity(arr):
    st=[]
    for i in range(len(arr)):
        st.append(i)
    while len(st)>1:
        i=st.pop()
        j=st.pop()
        if arr[i][j]==1:
            st.append(j)
        else:
            st.append(i)
    candidate=st.pop()
    for c in range(len(arr[0])):
        if arr[candidate][c]==1:
            print("None")
            return
    for r in range(len(arr)):
        if r!=candidate and arr[r][candidate]==0:
            print("None")
            return
    return candidate
arr=[[0,0,0,0],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
print(find_celebrity(arr))