"""
Docstring for 2026-leetcode.top-k-frequent


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


"""

# this solution has a run time of O(n)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary that will hold the a counter for each apperance of the numbers in nums'
        counter = {}
        # create the buckts that will catagorize nums by how may times they appear
        freq = [[] for i in range(len(nums) + 1)]

        # populate the counter hashmap
        for n in nums:
            # adds 1 to the counter[n] if present, if not then set to 0. either way add 1
            counter[n] = 1 + counter.get(n, 0)

        # create a loop that goes through each pair within count
        for n, c in counter.items():
            # using the count (c) as the index, store the numbers (n) that appear freq[c] times
            freq[c].append(n)

        # create the result list
        res = []

        # loop through freq starting for the last index
        for i in range(len(freq) - 1, 0, -1):
            # loop through each bucket in freq and append the value to res.
            # this will happen until res is at the length of k
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
