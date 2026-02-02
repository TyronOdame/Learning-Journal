"""
Docstring for 2026-leetcode.subarray-sum-equals-k


You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-1,1,2], k = 2

Output: 4
Explanation: [2], [2,-1,1], [-1,1,2], [2] are the subarrays whose sum is equals to k.

Example 2:

Input: nums = [4,4,4,4,4,4], k = 4

Output: 6

"""

# this solution has a run time of O(n)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # this keeps track of the current sum of the subarray
        curr_sum = 0
        res = 0
        # this is the hashmap that keeps track of the prefix sums
        prefix_sums = {0: 1}

        # loop through the array
        for n in nums:
            curr_sum += n
            diff = curr_sum - k

            res += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        return res
