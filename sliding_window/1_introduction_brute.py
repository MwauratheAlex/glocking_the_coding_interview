#!/usr/bin/python3

"""given an array, find average of all contiguous subarrays of size K in it"""

def find_average_of_subarrays(K, arr):
    """bruteforce approach"""
    result = []

    for i in range(len(arr) - K + 1):
        _sum = 0.0
        # find sum of next 'K' elements
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K) #calculate average

    return result

def main():
    result = find_average_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])

    print("Averages of subarrays of size K: " + str(result))

main()
