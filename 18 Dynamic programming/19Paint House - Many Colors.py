def paintHouseManyColors(cost):
    n=len(cost)
    k=len(cost[0])
    dp=[[0 for i in range(k)] for j in range(n)]
    min=int(1e9)
    smin=int(1e9)
    for i in range(n):
        nmin=int(1e9)
        nsmin=int(1e9)
        for j in range(k):
            if i==0:
                dp[i][j]=cost[i][j]
            else:
                if cost[i-1][j]!=min:
                    dp[i][j]=cost[i][j]+min
                else:
                    dp[i][j]=cost[i][j]+smin
            if dp[i][j]<=nmin:
                nsmin=nmin
                nmin=dp[i][j]
            elif dp[i][j]<nsmin:
                nsmin=dp[i][j]
        min=nmin
        smin=nsmin
    return min
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
print(paintHouseManyColors(paints))