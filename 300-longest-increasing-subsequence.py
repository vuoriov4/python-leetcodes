class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [] # (x, len)
        result = 1
        for i in range(0, len(nums)):
            x = nums[i]
            if (i == 0):
                dp.append((x, 1))
            else:
                j = i - 1
                l = 1
                while (j >= 0):
                    if (dp[j][0] < x):
                        l = max(l, dp[j][1] + 1)
                    elif (l > j):
                        break
                    j -= 1
                dp.append((x, l))
                result = max(result, l)
        return result
