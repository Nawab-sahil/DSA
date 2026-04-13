class Solution(object):
    def getMinDistance(self, nums, target, start):
        for d in range(len(nums)):
            if start - d >= 0 and nums[start - d] == target:
                return d
            if start + d < len(nums) and nums[start + d] == target:
                return d