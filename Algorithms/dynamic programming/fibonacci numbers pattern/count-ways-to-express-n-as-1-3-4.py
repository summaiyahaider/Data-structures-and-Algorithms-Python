'''
Given n, count the number of ways to express n as sum of 1, 3 and 4 modulo (109+7).

Example 1:

Input:
n = 1
Output:
1
Explanation:
There is only one way to represent 1 as
sum of 1,3 and 4. 1 = {1}.
Example 2:

Input:
n = 3
Output:
2
Explanation:
There is 2 ways to represent 3 as sum
of 1,3 and 4. 3 = {1,1,1}, and 3 = {3}.

constraints:
1 <= n <= 105

problem-link:
https://practice.geeksforgeeks.org/problems/count-ways-to-express-n-as-the-sum-of-13-and-44024/1/#
'''

# brute force solution
def countWays(n):
  def rec(x):
    if x == 0: return 1
    if x < 0: return 0
    pos1 = rec(x-1)
    pos2 = rec(x-3)
    pos3 = rec(x-4)
    return pos1 + pos2 + pos3
  return rec(n) % (10**9 + 7)

# top down with memoization
def countWays(n):
  dp = [-1 for _ in range(n+1)]
  def rec(x):
    if x == 0: return 1
    if x < 0: return 0
    if dp[x] == -1:
      pos1 = rec(x-1)
      pos2 = rec(x-3)
      pos3 = rec(x-4)
      dp[x] = pos1 + pos2 + pos3
    return dp[x]
  return rec(n) % (10**9 + 7)

# bottom up approach
def countWays(n):
  if n <= 2: return 1
  if n == 3: return 2
  if n == 4: return 4
  dp = [-1 for _ in range(n+1)]
  dp[-1] = 1
  dp[-2] = 1
  dp[-3] = 1
  dp[-4] = 2
  for i in range(n-4, -1, -1):
    dp[i] = dp[i+1] + dp[i+3] + dp[i+4]
  return dp[0]
  




