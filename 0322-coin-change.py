from fractions import gcd
from functools import reduce

class Solution(object):
    
    def find_gcd(self, list):
        x = reduce(gcd, list)
        return x
    
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = []
        gcd = self.find_gcd(coins)
        if (amount == 0): return 0
        if (amount % gcd != 0): return -1
        x = 0
        while (x <= amount):
            if (x in coins): 
                dp.append(1)
            else:
                res = -1
                for c in coins:
                    if (x - c >= 0 and dp[(x - c) // gcd] >= 0):
                        y = 1 + dp[(x - c) // gcd]
                        res = y if res == -1 else min(res, y)
                dp.append(res)
            x += gcd
        return dp[amount // gcd]
        
