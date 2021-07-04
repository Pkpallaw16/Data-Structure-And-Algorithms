def print_ways_select_boxes_2d(n,m,r,c,bsf,asf):
    if r==n:
        print(asf)
        return

    if c+1<m:
        print_ways_select_boxes_2d(n,m,r,c+1,bsf+1,asf+"("+str(r)+"-"+str(c)+")")
    else:
        print_ways_select_boxes_2d(n, m, r+1, 0, bsf + 1, asf + "(" + str(r) + "-" + str(c) + ")")

    if c+1<m:
        print_ways_select_boxes_2d(n,m,r,c+1,bsf,asf)
    else:
        print_ways_select_boxes_2d(n, m, r+1, 0, bsf, asf )

print_ways_select_boxes_2d(2,2,0,0,0,"")