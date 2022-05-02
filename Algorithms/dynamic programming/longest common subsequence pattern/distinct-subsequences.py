'''
question:
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag

constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.

problem-link:
https://leetcode.com/problems/distinct-subsequences/
'''

# brute forcee solution
def numDistinct(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    def rec(i1, i2):
        if i2 >= n2: return 1
        if i1 >= n1: return 0
        c1 = c2 = 0
        if s1[i1] == s2[i2]:
            c1 = rec(i1+1, i2+1)
        c2 = rec(i1+1, i2)
        return c1 + c2
    return rec(0, 0)

# top down with memomization
def numDistinct(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[-1 for _ in range(n2)] for _ in range(n1)]
    def rec(i1, i2):
        if i2 >= n2: return 1
        if i1 >= n1: return 0
        if dp[i1][i2] == -1:
            c1 = c2 = 0
            if s1[i1] == s2[i2]:
                c1 = rec(i1+1, i2+1)
            c2 = rec(i1+1, i2)
            dp[i1][i2] = c1 + c2
        return dp[i1][i2]
    return rec(0, 0)
