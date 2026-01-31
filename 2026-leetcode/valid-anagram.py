"""
Docstring for 2026-leetcode.valid-anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false


"""

# this solution has a run time of O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # guard clause for different lengths
        if len(s) != len(t):
            return False

        # create the hashmap to hold the count for each letter in s
        s_count = {}

        # add each letter in s to the hashmap and keep count of how many of each letter is present
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        # iterate through each letter in t and decrement the count in the hashmap
        for char in t:
            if char not in s_count:
                return False
            else:
                s_count[char] -= 1

        # check if all the values in the hashmap are 0
        for vals in s_count.values():
            if vals != 0:
                return False

        return True
