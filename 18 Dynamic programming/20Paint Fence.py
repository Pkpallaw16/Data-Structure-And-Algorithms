def Paint_Fence(fence,paint):
    same_color=paint
    diff_color=paint*(paint-1)
    for i in range(3,fence+1):
        print(diff_color, same_color)
        new_same_color=diff_color
        new_diff_color=(same_color+diff_color)*(paint-1)
        diff_color=new_diff_color
        same_color=new_same_color

    print(diff_color+same_color)

Paint_Fence(8,3)