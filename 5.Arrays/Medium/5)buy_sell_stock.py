# brute
def maxProfit(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit


# better
def maxProfit2(prices):
    mini = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        cost = prices[i] - mini
        profit = max(profit, cost)
        mini = min(mini, prices[i])
    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit2(prices))
print(maxProfit(prices))
