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

n=int(input("enter number of house: "))
paints=[[int(c) for c in input().split()] for i in range(n)]
Paint_House(paints)