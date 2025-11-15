/*
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

*/

function longestConsecutive(nums) {
  // take nums and put all the values into a set
  const numSet = new Set(nums);

  // create a variable to hold the length of the longest conseq. numbers
  let longest = 0;

  // go through every number inside of the numSet
  for (let num of numSet) {
    // check if the current num is the start of a sequence
    if (!numSet.has(num - 1)) {
      // create a var. that holds the lengthof the current sequence.
      let length = 1;

      // we can also use length to do the incrementation on num for the conseq. sequence
      while (numSet.has(num + length)) {
        length++;
      }
      // take the bigger number as the length between longest and length
      longest = Math.max(longest, length);
    }
  }
  return longest;
}
