'''
question:
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.

problem-link:
https://leetcode.com/problems/longest-palindromic-subsequence/
'''

# brute force solution
def longestPalindromeSubseq(s):
    n = len(s)
    def rec(i, j):
        if i > j: return 0
        if i == j: return 1
        pos1 = pos2 = pos3 = 0
        if s[i] == s[j]:
            pos1 = 2 + rec(i+1, j-1)
        pos2 = rec(i, j-1)
        pos3 = rec(i+1, j)
        return max(pos1, pos2, pos3)
    return rec(0, n-1)

# top down with memoization
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    def rec(i, j):
        if i > j: return 0
        if i == j: return 1
        if dp[i][j] == -1:
            pos1 = pos2 = pos3 = 0
            if s[i] == s[j]:
                pos1 = 2 + rec(i+1, j-1)
            pos2 = rec(i, j-1)
            pos3 = rec(i+1, j)
            dp[i][j] = max(pos1, pos2, pos3)
        return dp[i][j]
    return rec(0, n-1)