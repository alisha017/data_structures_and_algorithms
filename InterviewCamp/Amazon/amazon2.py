def ideal_days(days, k):
    days_decreasing = [0] * len(days)
    days_increasing = [0] * len(days)

    for i in range(1, len(days) - 1):
        if days[i] <= days[i - 1]:
            days_decreasing[i] = days_decreasing[i - 1] + 1

    for i in range(len(days) - 2, -1, -1):
        if days[i] <= days[i + 1]:
            days_increasing[i] = days_increasing[i + 1] + 1

    result = [
        (i, min(i, j))
        for i, (i, j) in enumerate(zip(days_increasing, days_decreasing))
    ]
    solution = [i + 1 for i, day in result if day >= k]

    return solution
