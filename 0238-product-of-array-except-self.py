class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        cumprod = 1
        for i in range(0, len(nums), 1):
            result.append(cumprod)
            cumprod *= nums[i]
        cumprod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= cumprod
            cumprod = cumprod * nums[i]
        return result
