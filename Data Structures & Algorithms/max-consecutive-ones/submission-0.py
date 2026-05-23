class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        maxout = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                output += 1
            else:
                output = 0
            maxout = max(maxout, output)
        return maxout
