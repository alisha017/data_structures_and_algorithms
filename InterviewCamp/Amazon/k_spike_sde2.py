def count_k_spikes(prices, k):
    n = len(prices)
    left_count = [0] * n
    right_count = [0] * n

    # Calculate the count of elements smaller than the current element to the left
    for i in range(1, n):
        count = 0
        for j in range(i - 1, -1, -1):
            if prices[j] < prices[i]:
                count += 1
                if count >= k:
                    left_count[i] = count
                    break

    # Calculate the count of elements smaller than the current element to the right
    for i in range(n - 2, -1, -1):
        count = 0
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                count += 1
                if count >= k:
                    right_count[i] = count
                    break

    # Count the number of k-spikes
    k_spikes_count = 0
    for i in range(n):
        if left_count[i] >= k and right_count[i] >= k:
            k_spikes_count += 1

    return k_spikes_count

# Example

if __name__ == "__main__":
    prices = [1, 2, 8, 5, 3, 4]
    k = 2
    result = count_k_spikes(prices, k)
    print(result)  # Output: 2
