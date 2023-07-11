#!/usr/bin/python3

"""Given a string, find the length of the longest substring which has no repeating characters."""
def no_repeat_substring(string):
    window_start = 0
    max_len = 0
    char_idx_map = {}
    
    #Extend the window [window_start, window_end]
    for window_end in range(len(string)):
        right_char = string[window_end]

        #If the hashmap has the character, shrink until we can only have one
        if right_char in char_idx_map:
            right_char_idx = char_idx_map[right_char]
            window_start = max(right_char_idx + 1, window_start)

        char_idx_map[right_char] = window_end
        max_len = max(max_len, window_end - window_start + 1)

    return max_len

def main():
    print(no_repeat_substring("aabccbb"))
    print(no_repeat_substring("abbbb"))
    print(no_repeat_substring("abccde"))

main()
