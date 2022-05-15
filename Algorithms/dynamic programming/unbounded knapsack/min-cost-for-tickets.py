'''
question:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

constraints:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000

problem-link:
https://leetcode.com/problems/minimum-cost-for-tickets/
'''



# brute force solution
def mincostTickets(days, costs):
    last_day = days[-1]
    first_day = days[0]
    days = set(days)
    def rec(exp_day):
        if exp_day > last_day: return 0
        if exp_day in days:
            pos1 = costs[0] + rec(exp_day+1)
            pos2 = costs[1] + rec(exp_day+7)
            pos3 = costs[2] + rec(exp_day+30)
            return min(pos1, pos2, pos3)
        else:
            return rec(exp_day+1)
    return rec(first_day)

# top down with memoization
def mincostTickets(days, costs):
    last_day = days[-1]
    first_day = days[0]
    days = set(days)
    dp = [-1 for _ in range(last_day+1)]
    def rec(exp_day):
        if exp_day > last_day: return 0
        if dp[exp_day] == -1:
          if exp_day in days:
              pos1 = costs[0] + rec(exp_day+1)
              pos2 = costs[1] + rec(exp_day+7)
              pos3 = costs[2] + rec(exp_day+30)
              dp[exp_day] = min(pos1, pos2, pos3)
          else:
              dp[exp_day] = rec(exp_day+1)
        return dp[exp_day]
    return rec(first_day)