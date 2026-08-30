class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 1, n - 1

        while low < high:
            lessOrEqual = 0
            mid = (low + high) // 2
            for num in nums:
                if num <= mid:
                    lessOrEqual += 1
            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid
        return low

        