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
    # max_diff_ = 0
    #
    # for curr_stock_price in stock_price_list:
    #     min_so_far = min(min_so_far, curr_stock_price)
    #     diff = curr_stock_price - min_so_far
    #
    #     if diff > max_diff:
    #         max_diff = diff

    for i in range(len(stock_price_list)-1, -1, -1):
        pass


if __name__ == '__main__':
    array: List[List[int]] = [[1, 3, 5, 2, 6, 4, 7, 8, 9], [9, 3, 2, 1, 5, 7, 2, 8, 3, 4]]

    for stocks in array:
        print(get_max_profit(stocks))

    get_max_profit_upto_2(array[0])
