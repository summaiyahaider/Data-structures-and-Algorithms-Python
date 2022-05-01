'''
question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400

problem-link:
https://leetcode.com/problems/house-robber/
'''

# brute force solution
def rob(nums):
  n = len(nums)

  def rec(idx):
    if idx >= n: return 0
    pos1 = nums[idx] + rec(idx+2)
    pos2 = rec(idx+1)
    return max(pos1, pos2)

  return rec(0)

# top down with memoization
def rob(nums):
  n = len(nums)
  dp = [-1 for _ in range(n)]
  
  def rec(idx):
    if idx >= n: return 0
    if dp[idx] != -1: return dp[idx]
    pos1 = nums[idx] + rec(idx+2)
    pos2 = rec(idx+1)
    dp[idx] = max(pos1, pos2)
    return dp[idx]
  
  return rec(0)

# bottom up approach
def rob(nums):
  n = len(nums)
  if n <= 1: return sum(nums)
  dp = [-1 for _ in range(n)]
  dp[-1] = nums[-1]
  dp[-2] = max(nums[-2], nums[-1])
  for i in range(n-3, -1, -1):
    dp[i] = max(dp[i+1], nums[i] + dp[i+2])
  return dp[0]