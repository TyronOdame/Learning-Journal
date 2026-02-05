"""
Docstring for 2026-leetcode.flood-fill

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.



Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]





"""

# this solution has a run time of O(m*n)
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        # prevents infinte loop. checks if the starting pixel is already the new color
        if image[sr][sc] == color:
            return image

        # setting the rows and columns for the image
        m, n = len(image), len(image[0])

        
        dirs = [1, 0, -1, 0, 1]

        def dfs(r: int, c: int, org):
            if not (0 <= r < m) or not (0 <= c < n) or image[r][c] != org:
                return

        image[r][c] = color
            for d in range(4):
                dfs(r + dirs[d], c + dirs[d + 1], org)

        dfs(sr, sc, image[sr][sc])
        return image