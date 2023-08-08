from typing import List
import math


def get_max_profit(stock_price_list: List[int]):
    min_so_far = math.inf
    max_diff = 0

    for curr_stock_price in stock_price_list:
        min_so_far = min(min_so_far, curr_stock_price)
        diff = curr_stock_price - min_so_far

        if diff > max_diff:
            max_diff = diff

    return max_diff


def get_max_profit_upto_2(stock_price_list: List[int]):
    min_so_far = math.inf
    max_diff = 0
    best_till_i = [0] * len(stock_price_list)
    for i in range(len(stock_price_list)):
        min_so_far = min(min_so_far, stock_price_list[i])
        diff = stock_price_list[i] - min_so_far

        max_diff = max(max_diff, diff)
        best_till_i[i] = max_diff

    max_so_far = -math.inf
    max_diff = 0
    best_from_i = [0] * len(stock_price_list)
    for i in range(len(stock_price_list) - 1, -1, -1):
        max_so_far = max(max_so_far, stock_price_list[i])
        diff = max_so_far - stock_price_list[i]
        max_diff = max(diff, max_diff)
        best_from_i[i] = max_diff

    max_2_trades = 0
    print(f"Forward loop, best till i:  {best_till_i}")
    print(f"Backward loop, best from i: {best_from_i}")
    for i in range(len(stock_price_list)):
        max_second_trade = best_from_i[i + 1] if i + 1 < len(stock_price_list) else 0
        max_2_trades = max(max_2_trades, max_second_trade + best_till_i[i])

    return max_2_trades


if __name__ == '__main__':
    array: List[List[int]] = [[1, 3, 5, 2, 6, 4, 7, 8, 9], [9, 3, 2, 1, 5, 7, 2, 8, 3, 4], [5, 9, 4, 2, 9, 7, 6]]

    for stocks in array:
        print(get_max_profit(stocks))

        print(get_max_profit_upto_2(stocks))
