class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = dict()
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if (s_sorted not in result):
                result[s_sorted] = [s]
            else:
                result[s_sorted].append(s)
        return result.values()
