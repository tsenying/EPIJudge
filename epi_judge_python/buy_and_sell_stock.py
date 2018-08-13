from test_framework import generic_test


# O(n**2)
def x_buy_and_sell_stock_once(prices):
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
    min_price = prices[0]

    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        if profit > 0 and profit > max_profit:
            max_profit = profit
        if prices[i] < min_price:
            min_price = prices[i]
    return max_profit


P=[310,315,275,295,260,270,290,230,255,250]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
