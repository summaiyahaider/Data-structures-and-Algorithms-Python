'''
question:
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100

problem-link:
https://leetcode.com/problems/partition-equal-subset-sum/
'''

# brute force solution
def canPartition(nums):
    n = len(nums)
    total = sum(nums)
    if total % 2 != 0: return False
    target = total//2
    def rec(i, curr):
        if curr == target: return True
        if i >= n or curr > target: return False
        pos1 = rec(i+1, curr+nums[i])
        pos2 = rec(i+1, curr)
        return pos1 or pos2
    return rec(0, 0)

# top down with memomization
def canPartition(nums):
    n = len(nums)
    total = sum(nums)
    if total % 2 != 0: return False
    target = total//2
    dp = [[-1 for _ in range(target+1)] for _ in range(n)]
    def rec(i, curr):
        if curr == target: return True
        if i >= n or curr > target: return False
        if dp[i][curr] == -1:
            pos1 = rec(i+1, curr+nums[i])
            pos2 = rec(i+1, curr)
            dp[i][curr] = pos1 or pos2
        return dp[i][curr]
    return rec(0, 0)
