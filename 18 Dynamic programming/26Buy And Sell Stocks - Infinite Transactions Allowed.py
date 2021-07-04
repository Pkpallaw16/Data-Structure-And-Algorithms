
def Buy_And_Sell_Stocks_infinite_Transaction_Allowed(price):
    buy_day=0
    sell_day=0
    profit=0
    for day in range(len(price)):
        if price[day-1]>price[day]:
            profit+=price[sell_day]-price[buy_day]
            buy_day=day
            sell_day=day
        else:
            sell_day=day

    profit+=price[sell_day]-price[buy_day]

n=int(input("enter number of days: "))
price=[]
for i in range(n):
    price.append(int(input()))
print(Buy_And_Sell_Stocks_infinite_Transaction_Allowed(price,price[0],1))
