def smallest_number_following_patter(pattern):
    st=[]
    count=1
    for ch in pattern:
        if ch=='d':
            st.append(count)
            count+=1
        else:
            st.append(count)
            count+=1
            while len(st)>0:
                print(st.pop(),end="")
    st.append(count)
    while len(st) > 0:
        print(st.pop(), end="")
pattern=input("input pattern")
smallest_number_following_patter(pattern)