def maxProfit(prices):
    profit = 0
    minBuy = prices[0]

    for price in prices:
        profit = max(profit, price - minBuy)
        minBuy = min(minBuy, price)
    return profit

prices = [10,1,5,6,7,1]
print(maxProfit(prices))