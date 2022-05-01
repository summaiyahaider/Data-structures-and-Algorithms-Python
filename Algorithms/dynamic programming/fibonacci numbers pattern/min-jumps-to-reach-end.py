'''
question:
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000

problem-link:
https://leetcode.com/problems/jump-game-ii/
'''

# brute force solution
def jump(nums):
  last = len(nums) - 1
  def rec(idx):
    if idx == last: return 0
    if idx > last: return float('inf')
    curr_jumps = nums[idx]
    min_jumps = float('inf')
    for i in range(1, curr_jumps+1):
      min_jumps = min(min_jumps, 1 + rec(idx + i))
    return min_jumps
  return rec(0)

# top down with memoization
def jump(nums):
  last = len(nums) - 1
  dp = [-1 for _ in range(last)]
  def rec(idx):
    if idx == last: return 0
    if idx > last: return float('inf')
    if dp[idx] == -1:
      curr_jumps = nums[idx]
      min_jumps = float('inf')
      for i in range(1, curr_jumps+1):
        min_jumps = min(min_jumps, 1 + rec(idx + i))
      dp[idx] = min_jumps
    return dp[idx]
  return rec(0)

# bottom up approach
def jump(nums):
    last = len(nums) - 1
    dp = [float('inf') for _ in range(last+1)]
    dp[-1] = 0
    for i in range(last-1, -1, -1):
        curr_jumps = nums[i]
        for j in range(1, curr_jumps+1):
            if i + j <= last:
                dp[i] = min(dp[i], 1 + dp[i+j])
    return dp[0]