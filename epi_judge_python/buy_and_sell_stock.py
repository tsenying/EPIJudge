from test_framework import generic_test


# O(n**2)
def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    max_profit = 0.0
    for i in range(len(prices) - 1):
        for j in range(i, len(prices)):
            profit = prices[j] - prices[i]
            if profit > 0 and profit > max_profit:
                max_profit = profit
    return max_profit

def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    max_profit = 0.0
    per_day_profit = [0.0] * len(prices)
    for i in range(1, len(prices)):
        



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
