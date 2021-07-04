def Buy_And_Sell_Stocks_One_Transaction_Allowed(price):
    profit=0
    minimum_price=price[0]
    for day in range(1,len(price)):
        if price[day]<minimum_price:
            profit=max(profit,price[day]-minimum_price)
            minimum_price=min(minimum_price,price[day])
    return profit
def Buy_And_Sell_Stocks_one_Transaction_Allowed_rec(price,minimum,indx):
    if indx>=len(price):
        return 0
    if price[indx]<minimum:
        minimum=price[indx]
    profit=Buy_And_Sell_Stocks_one_Transaction_Allowed_rec(price,minimum,indx+1)
    if profit<price[indx]-minimum:
        profit=price[indx]-minimum
    return profit
n=int(input("enter number of days: "))
price=[]
for i in range(n):
    price.append(int(input()))
print(Buy_And_Sell_Stocks_One_Transaction_Allowed(price))
