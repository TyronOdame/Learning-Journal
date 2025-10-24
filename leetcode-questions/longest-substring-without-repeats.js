/*
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  // intialize the max length
  let maxlen = 0;
  let left = 0;
  const charIndex = new Map();

  // iterate throught the given string

  for (let right = 0; right < s.length; right++) {
    const curr = s[right];

    if (charIndex.has(curr) && charIndex.get(curr) >= left) {
      left = charIndex.get(curr) + 1;
    }

    charIndex.set(curr, right);
    maxlen = Math.max(maxlen, right - left + 1);
  }
  return maxlen;
};
