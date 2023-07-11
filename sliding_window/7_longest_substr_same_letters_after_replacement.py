#!/usr/bin/python3

"""Given a string with lowercase letters only, if you are allowed to replace
no more than ‘k’ letters with any letter, find the length of the longest substring
having the same letters after replacement."""

def length_of_longest_substring(string, k):
    window_start = 0
    max_len = 0
    max_count = 0
    freq_map = {}

    #Extend
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] += 1
        max_count = max(max_count, freq_map[right_char])

        #Shrink
        if (window_end - window_start + 1 - max_count) > k:
            left_char = string[window_start]
            freq_map[left_char] -= 1
            window_start += 1

        #Update max_len
        max_len = max(max_len, window_end - window_start + 1)


    return max_len

def main():
    print(length_of_longest_substring("aabccbb", k=2))
    print(length_of_longest_substring("abbcb", k=1))
    print(length_of_longest_substring("abccde", k=1))

main()
