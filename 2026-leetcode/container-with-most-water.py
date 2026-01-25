"""
Docstring for 2026-leetcode.container-with-most-water

You are given an integer array heights where heights[i] represents the height of the
i
t
h
i
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # created left and right pointers to point at opposite ends of the list
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # formula for checking area of the bottleneck height
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # increamenting the index of the pointer
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        # return the heightst area (held in res)
        return res
