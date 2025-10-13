/*
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

*/

/**
 * @param {number[]} nums
 * @return {number}

 Problem: Given a array of numbers (nums), return the number that appears more then n(n being the length of the array) / 2

 example:
    array = [4,4,4,4,4,1]
    output: 4


1.create a empty obj 

2.iterate through the array nums

3. at each index, check if the current value of that index is in the obj, if not then add it as a key and set it value to zero.

4. iterate through the obj and return the number that has apperaed more frequently
 */
var majorityElement = function (nums) {
  const obj = {};

  for (let i = 0; i < nums.length; i++) {
    let curr = nums[i];

    if (obj[curr]) {
      obj[curr]++;
    } else {
      obj[curr] = 1;
    }
  }

  for (keys in obj) {
    if (obj[keys] > nums.length / 2) {
      return parseInt(keys);
    }
  }
};
