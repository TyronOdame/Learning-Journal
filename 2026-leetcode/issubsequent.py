"""
Docstring for 2026-leetcode.issubsequent


Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        for char in s:
            if t.find(char) == -1:
                return False
        return True


# two pointer approach


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s

        for char in t:
            if i < len(s) and char == s[i]:
                i += 1

        return i == len(s)
