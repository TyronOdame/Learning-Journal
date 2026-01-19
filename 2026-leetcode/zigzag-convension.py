"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:


"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # handle case where numRows == 1
        if numRows == 1:
            return s

        res = ""  # this is what we will be returning

        # loop through the given number of rows (numRows)
        for r in range(numRows):
            increment = 2 * (
                numRows - 1
            )  # this if the incrementation that will give the zigzag

            # loop through the string (s), start at r, end at length of s, increment by the equation (increment)
            for i in range(r, len(s), increment):
                res += s[i]  # add the first letter
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    res += s[i + increment - 2 * r]

        return res
