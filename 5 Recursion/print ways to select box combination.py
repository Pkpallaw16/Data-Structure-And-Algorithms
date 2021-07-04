def print_ways_to_select_box(cb,tb,asf):
    if cb==tb:
        print(asf)
        return
    print_ways_to_select_box(cb+1,tb,asf+"b"+str(cb)+" ")
    print_ways_to_select_box(cb+1,tb,asf)

print_ways_to_select_box(0,4,"")

def print_ways_to_select_n_box(cb,tb,bsf,asf):
    if cb==tb:
        if bsf==2:
            print(asf)
        return
    if bsf+1<=2:
        print_ways_to_select_box(cb+1,tb,bsf,asf+"b"+str(cb)+" ")
    print_ways_to_select_box(cb+1,tb,bsf,asf)

print_ways_to_select_n_box(0,4,0,"")