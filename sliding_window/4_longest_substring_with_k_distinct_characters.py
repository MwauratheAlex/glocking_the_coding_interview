#!/usr/bin/python3

"""Given a string, find the length of the longest substring
in it with no more than K distinct characters."""

def longest_substring_with_k_distinct(string, k):
    window_start = 0
    char_freq = {}
    max_len = 0

    #Expand the window
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        #Shrink the window
        while len(char_freq) > k:
            left_char = string[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1 #shrink the window
        #Remember the length
        max_len = max(max_len, window_end - window_start + 1)

    return max_len

def main():
    print(longest_substring_with_k_distinct("araaci", 2))
    print(longest_substring_with_k_distinct("araaci", 1))
    print(longest_substring_with_k_distinct("cbbebi", 3))

main()
