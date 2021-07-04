def print_ways_select_one_in_column_boxes_2d(n,m,r,c,bsf,asf):
    if r==n:
        if bsf==2:
            print(asf)
        return

    if c+1<m:
        #yes call
        print_ways_select_one_in_column_boxes_2d(n,m,r+1,0,bsf+1,asf+"("+str(r)+"-"+str(c)+")")
        #no call
        print_ways_select_one_in_column_boxes_2d(n, m, r, c+1, bsf,asf)

    else:
        #yes call
        print_ways_select_one_in_column_boxes_2d(n,m,r+1,0,bsf+1,asf+"("+str(r)+"-"+str(c)+")")
        #no call
        print_ways_select_one_in_column_boxes_2d(n, m, r+1, 0, bsf, asf )

print_ways_select_one_in_column_boxes_2d(2,2,0,0,0,"")