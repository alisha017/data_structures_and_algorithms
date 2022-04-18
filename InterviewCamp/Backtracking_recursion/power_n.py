#TODO 

def get_x_power_n(x, n, power_map):
    if n == 0:
        return x
    if power_map.get(n):
        return power_map[n]

    result = get_x_power_n(x, n-1, power_map)
    power_map[n] = result
    return result


if __name__ == '__main__':
    print(get_x_power_n(2, 4, {}))

