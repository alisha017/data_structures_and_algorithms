from typing import List


def coin_change_count(target:int, coins: List[int]):
    coins_combinations = [0]*(target+1)
    coins_combinations[0] = 1

    for coin in coins:
        for i in range(coin, target + 1):
            coins_combinations[i] += coins_combinations[i-coin]

    return coins_combinations[-1]


if __name__ == "__main__":
    print(coin_change_count(5, [1, 2, 5]))
    print(coin_change_count(11, [1, 2, 5]))
    print(coin_change_count(3, [2]))
