class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return len([1 for i in range(0, 32) if (1 << i) & n > 0])
