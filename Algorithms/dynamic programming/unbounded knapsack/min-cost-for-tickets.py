



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