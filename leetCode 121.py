# Best time to buy and sell stock


def maxProfit(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell

    return profit


prices = [3, 5, 6, 7, 8, 5, 1, 7, 64, 0]
maxProfit(prices)
