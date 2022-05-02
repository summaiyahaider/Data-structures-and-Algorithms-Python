'''
question:
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

problem-link:
https://leetcode.com/problems/longest-common-subsequence/
'''

# brute force solution
def lcs(text1, text2):
  n1 = len(text1)
  n2 = len(text2)

  def rec(i1, i2):
    if i1 >= n1 or i2 >= n2:
      return 0
    c1 = c2 = c3 = 0
    if text1[i1] == text2[i2]:
      c1 = 1 + rec(i1+1, i2+1)
    c2 = rec(i1+1, i2)
    c3 = rec(i1, i2+1)
    return max(c1, c2,  c3)
  return rec(0, 0)

# top down with memoization
def lcs(text1, text2):
  n1 = len(text1)
  n2 = len(text2)
  dp = [[-1 for _ in range(n2)] for _ in range(n1)]
  def rec(i1, i2):
    if i1 >= n1 or i2 >= n2:
      return 0
    if dp[i1][i2] != -1: return dp[i1][i2]
    c1 = c2 = c3 = 0
    if text1[i1] == text2[i2]:
      c1 = 1 + rec(i1+1, i2+1)
    c2 = rec(i1+1, i2)
    c3 = rec(i1, i2+1)
    dp[i1][i2] = max(c1, c2,  c3)
    return dp[i1][i2]
  return rec(0, 0)

# bottom up approach
def lcs(text1, text2):
  n1 = len(text1)
  n2 = len(text2)
  dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  for i1 in range(n1-1, -1, -1):
    for i2 in range(n2-1, -1, -1):
      if text1[i1] == text2[i2]:
        dp[i1][i2] = 1 + dp[i1+1][i2+1]
      else:
        dp[i1][i2] = max(dp[i1+1][i2], dp[i1][i2+1])
  return dp[0][0] 


