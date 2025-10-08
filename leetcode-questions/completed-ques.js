/*
Greatest Common Divisor of Strings
Solved 
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

You are given two strings str1 and str2, return the largest string x such that x divides both str1 and str2. If there is no such string, return "".

Example 1:

Input: str1 = "ABAB", str2 = "AB"

Output: "AB"
Example 2:

Input: str1 = "NANANA", str2 = "NANA"

Output: "NA"
Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

*/
class Solution {
  /**
   * @param {string} str1
   * @param {string} str2
   * @return {string}
   */
  gcdOfStrings(str1, str2) {
    // create variables the hold the lengths of the given strings
    const len1 = str1.length,
      len2 = str2.length;

    // option 1: create a function that checks to see if the length (l) modded the length of the words equals 0
    const isDivisor = (l) => {
      if (len1 % l !== 0 || len2 % l !== 0) {
        return false;
      }

      // this creates a sub string that decreases for the length of the whole string and down
      const sub = str1.slice(0, l);

      // this calculates how many times the l can go into len1. this will represent how many times
      //the sub string will fit into the length of the string

      const f1 = len1 / l,
        f2 = len2 / l;

      //this line of code allows us to check to see if the substrings repeated a f1 amount of times, would you get the original string
      return sub.repeat(f1) == str1 && sub.repeat(f2) == str2;
    };

    // create a for loop that sets the variable l to the string with the smallest length
    for (let l = Math.min(len1, len2); l > 0; l--) {
      // call the isDivisor function within a if condition to check if it returns true
      if (isDivisor(l)) {
        return str1.slice(0, l);
      }
    }
    return '';
  }
}
