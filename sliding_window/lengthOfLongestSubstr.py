#!/usr/bin/python3

def longestSubstringLength(s):
    max_len = 0
    window_start = 0
    char_idx_map = {}

    for window_end in range(len(s)):
        right_char = s[window_end]

        if right_char in char_idx_map:
            left_char_idx = char_idx_map[right_char]
            window_start = max(window_start, left_char_idx + 1)
        char_idx_map[right_char] = window_end
        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(longestSubstringLength("abcabcbb"))


