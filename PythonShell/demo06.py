def getMaxSubsequenceLen(arr):
    n = len(arr)
    result = []

    for i in range(n):
        count_less = 0
        count_greater = 0

        # Count distinct elements less than and greater than arr[i]
        for j in range(n):
            if arr[j] < arr[i]:
                count_less += 1
            elif arr[j] > arr[i]:
                count_greater += 1

        # Calculate the length of longest odd-length subsequence
        min_count = min(count_less, count_greater)
        max_odd_length = min_count * 2 + 1

        result.append(max_odd_length)

    return result


# Sample Input
arr = [3, 4, 1, 5, 1, 2, 2, 2]
print(getMaxSubsequenceLen(arr))
