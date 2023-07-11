#!/usr/bin/python3
"""Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’."""

def max_sum_subarray(K, arr):
    result = 0
    windowSum = 0.0
    windowStart = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]

        if windowEnd >= K - 1:
            result = max(windowSum, result)
            windowSum -= arr[windowStart]
            windowStart += 1
    return result

def main():
    result = max_sum_subarray(3, [2, 1, 5, 1, 3, 2])
    print("max_sub_array_of_size_k: " + str(result))
    print("max_sub_array_of_size_k: " + str(max_sum_subarray(2, [2, 3, 4, 1, 5])))

main()
