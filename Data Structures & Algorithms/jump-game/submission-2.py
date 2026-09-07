class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxlevel = 0
        levelreached = 0
        n = len(nums)
        jump =0
        for i in range(n - 1):
            levelreached = i
            jump = nums[i]
            if jump == 0:
                if maxlevel > i:
                    continue
                else:
                    break
            while jump > 0:
                levelreached = i + jump
                jump -= 1
                maxlevel = max(levelreached, maxlevel)
        if maxlevel >= n - 1:
            return True
        else:
            return False 


        
        