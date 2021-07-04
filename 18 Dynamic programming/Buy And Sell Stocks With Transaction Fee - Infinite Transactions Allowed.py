
def Buy_And_Sell_Stocks_infinite_Transaction_Allowed_Transaction_fee(price,trans_fee):
    buy_day=0
    sell_day=0
    profit=0
    for day in range(len(price)):
        if price[day-1]>price[day]:
            profit_now=price[sell_day]-price[buy_day]
            if profit_now>trans_fee:
                profit+=profit_now-trans_fee
            buy_day=day
            sell_day=day
        else:

            sell_day=day
    profit_now = price[sell_day] - price[buy_day]
    if profit_now>trans_fee:
        profit+=price[sell_day]-price[buy_day]-trans_fee
    return profit
n=int(input("enter number of days: "))
price=[]
for i in range(n):
    price.append(int(input()))
print(Buy_And_Sell_Stocks_infinite_Transaction_Allowed_Transaction_fee(price,3))
