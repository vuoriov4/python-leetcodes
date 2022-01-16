class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            loc = 31 - i
            bit = (n & (1 << loc)) >> loc
            result += bit << i
        return result
