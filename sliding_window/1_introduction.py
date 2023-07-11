#!/usr/bin/python3
""" given an array, find the average of all contingous subarrays of size 'K'"""

def find_avg_of_subarray(K, arr):
    """sliding window"""
    result = []
    windowSum = 0.0
    windowStart = 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] #add the next element
        #slide window after first K elements
        if windowEnd >= K - 1:
            result.append(windowSum / K) #calculate average
            windowSum -= arr[windowStart] #subtreact outgoing element
            windowStart += 1 #slide the window ahead

    return result

def main():
    result = find_avg_of_subarray(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main()
