'''
question:
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1

constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

problem-link:
https://leetcode.com/problems/target-sum/
'''

# brute force solution
def findTargetSumWays(nums, target):
    n = len(nums)
    def rec(i, curr):
        if i == n and curr == target: return 1
        if i == n: return 0
        pos1 = pos2 = 0
        pos1 = rec(i+1, curr + nums[i])
        pos2 = rec(i+1, curr + -nums[i])
        return pos1 + pos2
    return rec(0, 0)

# top down with memoization
def findTargetSumWays(nums, target):
    n = len(nums)
    dp = {}
    def rec(i, curr):
        key = str(i) + '$' + str(curr)
        if key in dp: return dp[key]
        if i == n and curr == target: return 1
        if i == n: return 0
        pos1 = pos2 = 0
        pos1 = rec(i+1, curr + nums[i])
        pos2 = rec(i+1, curr + -nums[i])
        dp[key] = pos1 + pos2
        return dp[key]
    return rec(0, 0)