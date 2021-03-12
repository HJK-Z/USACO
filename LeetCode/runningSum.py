# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            rsum.append(total)
            
        return rsum