#!/usr/bin/python3

"""Given a string with lowercase letters only, if you are allowed to replace
no more than ‘k’ letters with any letter, find the length of the longest substring
having the same letters after replacement."""

def length_of_longest_substring(string, k):
    return -1

def main():
    print(length_of_longest_substring("aabccbb", k=2))
    print(length_of_longest_substring("abbcb", k=1))
    print(length_of_longest_substring("abccde", k=1))

main()
