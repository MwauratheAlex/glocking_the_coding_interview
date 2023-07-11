#!/usr/bin/python3

"""Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit."""

def fruits_into_baskets(fruits):
    window_start = 0
    max_fruits = 0
    fruit_freq = {}

    #Extend the window
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        #Shrink the window
        while len(fruit_freq) > 2: #2 baskets provided
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1 #Shrink
        #Remember the max length
        max_fruits = max(max_fruits, window_end - window_start + 1)

    return max_fruits

def main():
    print(fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))
    print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))

main()
