'''
question:
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

problem-link:
https://leetcode.com/problems/longest-increasing-subsequence/
'''

# brute force solution
def lengthOfLIS(nums):
    n = len(nums)
    def rec(i, j):
        if j >= n: return 0
        c1 = c2 = 0
        if i == -1 or nums[j] > nums[i]:
            c1 = 1 + rec(j, j+1)
        c2 = rec(i, j+1)
        return max(c1, c2)
    return rec(-1, 0)

# top down with memoization
def lengthOfLIS(nums):
    n = len(nums)
    dp = [[-1 for _ in range(n)] for _ in range(n+1)]
    def rec(i, j):
        if j >= n: return 0
        if dp[i+1][j] == -1:
          c1 = c2 = 0
          if i == -1 or nums[j] > nums[i]:
              c1 = 1 + rec(j, j+1)
          c2 = rec(i, j+1)
          dp[i+1][j] = max(c1, c2)
        return dp[i+1][j]
    return rec(-1, 0)

# bottom up approach
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)