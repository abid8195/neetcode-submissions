class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        
        if len(nums) == 1:
            return nums[-1]
        maxSum = nums[0]
        if nums:
            for i in range(len(nums)):
                sum += nums[i]
                maxSum = max(sum, maxSum)
                if sum < 0:
                    sum = 0
            
        return maxSum
        