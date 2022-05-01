'''
question: 
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

constraints:
1 <= n <= 45

problem-link:
https://leetcode.com/problems/climbing-stairs/
'''

# brute force solution
def climbStairs(n):
  def rec(x):
    if x > n: return 0
    if x == n: return 1
    return rec(x+1) + rec(x+2) 
  return rec(0)

# top down with memoization
def climbStairs(n):
  dp = [-1 for _ in range(n+1)]
  def rec(x):
    if x > n: return 0
    if x == n: return 1
    if dp[x] != -1: return dp[x]
    dp[x] = rec(x+1) + rec(x+2)
    return dp[x]
  return rec(0)

# bottom up approach
def climbStairs(n):
  if n == 1: return 1
  dp = [-1 for _ in range(n+1)]
  dp[-1] = 1
  dp[-2] = 1
  for i in range(n-2, -1, -1):
    dp[i] = dp[i+1] + dp[i+2]
  return dp[0]

