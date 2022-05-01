'''
question: 
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

constraints:
0 <= n <= 30

problem-link:
https://leetcode.com/problems/fibonacci-number/
'''

# brute force solution
def fib(n):
  if n <= 1: return n
  return fib(n-1) + fib(n-2)

# top down with memoization
def fib(n):
  dp = [-1 for _ in range(n+1)]

  def rec(x):
    if x <= 1: return x
    if dp[x] != -1: return dp[x]
    dp[x] = rec(x-1) + rec(x-2)
    return dp[x]
  
  return rec(n)

# bottom up approach
def fib(n):
  if n <= 1: return n
  dp = [-1 for _ in range(n+1)]
  dp[0] = 0
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]
