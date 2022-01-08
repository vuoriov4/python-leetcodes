class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        occurences = dict()
        for i in range(0, len(nums)):
            x = nums[i]
            if ((target - x) in occurences): 
                j = occurences[target - x]
                return [j, i]
            else:
                occurences[nums[i]] = i 
        return []
       
