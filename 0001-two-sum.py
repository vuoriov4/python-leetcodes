class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            x = nums[i]
            for j in range(i+1, len(nums)):
                y = nums[j]
                if (x + y == target): 
                    return [i, j]
        return []
        