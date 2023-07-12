#!/usr/bin/python3
"""Given a string and a pattern, find out if the string contains any permutation of the pattern."""


def find_permutation(string, pattern):
    if len(pattern) > len(string):
        return False
    string_freq = [0] * 26
    pattern_freq = [0] * 26
    matches = 0

    for i in range(len(pattern)):
        string_freq[ord(string[i]) - ord("a")] += 1
        pattern_freq[ord(pattern[i]) - ord("a")] += 1

    for i in range(26):
        matches += (1 if string_freq[i] == pattern_freq[i] else 0)

    window_start = 0
    for window_end in range(len(pattern), len(string)):
        if matches == 26:
            return True
        index = ord(string[window_end]) - ord("a")
        string_freq[index] += 1
        if string_freq[index] == pattern_freq[index]:
            matches += 1
        elif string_freq[index] == pattern_freq[index] + 1:
            matches -= 1

        index = ord(string[window_start]) - ord("a")
        string_freq[index] -= 1
        if string_freq[index] == pattern_freq[index]:
            matches += 1
        elif string_freq[index] == pattern_freq[index] - 1:
            matches -= 1
        window_start += 1

    return matches == 26


def main():
    print(find_permutation("oidbcaf", "abc"))
    print(find_permutation("bcdxabcdy", "bcdyabcdx"))
    print(find_permutation("aaacb", "abc"))
    print(find_permutation("odicf", "dc"))

main()
