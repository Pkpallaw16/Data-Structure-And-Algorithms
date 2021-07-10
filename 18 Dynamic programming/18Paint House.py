def paint_house(cost):
    red=0
    green=0
    blue=0
    for i in range(len(cost)):
        n_red=min(green,blue)+cost[i][0]
        n_green=min(red,blue)+cost[i][1]
        n_blue=min(red,green)+cost[i][2]
        red=n_red
        green=n_green
        blue=n_blue
    return min(n_red,n_green,n_blue)

def Paint_House(paints):
    min_cost=0
    selected_paint=-1
    for i in range(len(paints)):
        min=int(1e9)
        for j in range(len(paints[0])):
            if selected_paint==j:
                continue
            if paints[i][j]<min:
                min=paints[i][j]
                selected_paint=j
        min_cost+=paints[i][selected_paint]
    print(min_cost)
def Paint_House_recursion(paints,last_paint,index):
    if index==-1:
        return 0
    min_cost=int(1e9)
    min_index=-1
    if last_paint!=0:
        min_cost=min(min_cost,Paint_House_recursion(paints,index-1,))
    Paint_House_recursion(paints, selected_paint, index, cost)

n=int(input("enter number of house: "))
paints=[[int(c) for c in input().split()] for i in range(n)]
Paint_House(paints)