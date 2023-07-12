#!/usr/bin/python3

"""Given a string and a pattern, find out if the string contains any permutation of the pattern."""

def find_permutation(s, pattern):
    matched = 0
    char_freq = {}
    window_start = 0

    for c in pattern:
        if c not in char_freq:
            char_freq[c] = 0
        char_freq[c] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1
        if len(char_freq) == matched:
            return True

        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1

    return False

def main():
    print(find_permutation("oidbcaf", "abc"))
    print(find_permutation("odicf", "dc"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("aaacb", "abc"))

main()
                
