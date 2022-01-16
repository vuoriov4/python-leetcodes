class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        for i in range(0, n+1):
            if (i == 0):
                dp.append(0)
            elif (i == 1):
                dp.append(1)
            elif (i == 2):
                dp.append(2)
            else:
                dp.append(dp[i-1] + dp[i-2])
        return dp[-1]
