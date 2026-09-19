class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxjump = 0
        curr_end = 0
        jumplength = 0
        if n <= 1:
            return 0
        for i in range(n - 1):
            maxjump = max(maxjump, i + nums[i])
            if i == curr_end:
                jumplength += 1
                curr_end = maxjump
                if curr_end >= n - 1:
                    break
        return jumplength
