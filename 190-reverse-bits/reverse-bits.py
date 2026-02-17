class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        
        for _ in range(32):
            # Shift result left to make space
            result <<= 1
            
            # Add last bit of n to result
            result |= (n & 1)
            
            # Shift n right to process next bit
            n >>= 1
            
        return result
