class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            l, r = 0, len(nums) - 1
            bound = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    bound = m
                    if isFirst: r = m - 1
                    else: l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return bound
        
        return [findBound(True), findBound(False)]