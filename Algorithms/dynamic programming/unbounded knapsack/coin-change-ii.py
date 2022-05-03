'''
question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000

problem-link:
https://leetcode.com/problems/coin-change-2/
'''

# brute force solution
def change(amount, coins):
    n = len(coins)
    def rec(i, curr):
        if curr > amount or i >= n: return 0
        if curr == amount: return 1
        pos1 = rec(i+1, curr)
        pos2 = rec(i, curr+coins[i])
        return pos1 + pos2
    return rec(0, 0)

#  top down with memoization
def change(amount, coins):
    n = len(coins)
    dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
    def rec(i, curr):
        if curr > amount or i >= n: return 0
        if curr == amount: return 1
        if dp[i][curr] == -1:
          pos1 = rec(i+1, curr)
          pos2 = rec(i, curr+coins[i])
          dp[i][curr] = pos1 + pos2
        return dp[i][curr]
    return rec(0, 0)


