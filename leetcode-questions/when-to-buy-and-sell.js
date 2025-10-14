/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

*/

/**
 * @param {number[]} prices
 * @return {number}


 problem: you are given a array of market prices for each day (prices), find out the total profit you can make if you buy on one day and sell on the other, if no profit can be made, return 0

 1. create a curr var that keeps track of the lowest price we have seen so far, set it to the first price in the array
 2. create a profit variable that keeps track of the total profit that has been made if sold 
 3. iterate through the given prices array starting from 1 (since we preset curr to the first price)
    - if the current price is less than curr, set curr to the current price
    - else, calculate the potential profit by subtracting curr from the current price
        - if the potential profit is greater than profit, set profit to potential profit
 4. return profit
 */
var maxProfit = function (prices) {
  let curr = prices[0];
  let profit = 0;

  let i = 1;
  while (i < prices.length) {
    if (prices[i] < curr) {
      curr = prices[i];
    } else {
      let potentialProfs = prices[i] - curr;

      if (potentialProfs > profit) {
        profit = potentialProfs;
      }
    }

    i++;
  }
  return profit;
};
