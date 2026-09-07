class Solution:

    def canJump(self, nums: List[int]) -> bool:

        maxlevel = 0
        n = len(nums)

        if n <= 1:
            return True

        for i in range(n - 1):

            if i > maxlevel:
                break

            maxlevel = max(maxlevel, i + nums[i])

            if maxlevel >= n - 1:
                return True

        return False


        
        