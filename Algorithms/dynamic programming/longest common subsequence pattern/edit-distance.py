'''
question:
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

constraints:
0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

problem-link:
https://leetcode.com/problems/edit-distance/
'''

# brute force solution
def minDistance(s1, s2):
    n1, n2 = len(s1), len(s2)
    def recursive(i1, i2):
        if i1 == n1:
            return n2 - i2 
        if i2 == n2:
            return n1 - i1
        if s1[i1] == s2[i2]:
            return recursive(i1+1, i2+1)
#           perform edit
        c1 = 1 + recursive(i1+1, i2+1)
#           perform insertion
        c2 = 1 + recursive(i1, i2+1)
#           perform deletion
        c3 = 1 + recursive(i1+1, i2)
        return min(c1, c2, c3)
    return recursive(0, 0)

# top down with memoization
def minDistance(s1, s2):
    n1, n2 = len(s1), len(s2)
    mem = {}
    def recursive(i1, i2):
        if i1 == n1:
            return n2 - i2 
        if i2 == n2:
            return n1 - i1
        key = str(i1) + '-' + str(i2)
        if key in mem: return mem[key]
        
        if s1[i1] == s2[i2]:
            return recursive(i1+1, i2+1)
#           perform edit
        c1 = 1 + recursive(i1+1, i2+1)
#           perform insertion
        c2 = 1 + recursive(i1, i2+1)
#           perform deletion
        c3 = 1 + recursive(i1+1, i2)
        mem[key] = min(c1, c2, c3)
        return mem[key]
    return recursive(0, 0)


