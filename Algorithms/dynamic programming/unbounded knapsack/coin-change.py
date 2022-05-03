'''
question:
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

problem-link:
https://leetcode.com/problems/coin-change/
'''

# brute force solution
def coinChange(coins, amount):
    n = len(coins)
    def rec(i, curr):
        if curr == amount: return 0
        if curr > amount or i >= n: return float('inf')
        pos1 = 1 + rec(i, curr+coins[i])
        pos2 = 1 + rec(i+1, curr+coins[i])
        pos3 = rec(i+1, curr)
        return min(pos1, pos2, pos3)
    res = rec(0, 0)
    return res if res != float('inf') else -1

# top down with memomization
def coinChange(coins, amount):
    if amount == 0: return 0
    n = len(coins)
    dp = [[-1 for _ in range(amount+1)] for _ in range(n)]
    def rec(i, curr):
        if curr == amount: return 0
        if curr > amount or i >= n: return float('inf')
        if dp[i][curr] == -1:
          pos1 = 1 + rec(i, curr+coins[i])
          pos2 = 1 + rec(i+1, curr+coins[i])
          pos3 = rec(i+1, curr)
          dp[i][curr] = min(pos1, pos2, pos3)
        return dp[i][curr]
    rec(0, 0)
    res = dp[0][0]
    return res if res != float('inf') else -1

