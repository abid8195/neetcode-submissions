class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        t = len(nums)
        for n in nums:
            if n in d1:
                d1[n] += 1
            else:
                d1[n] = 1
        output = []
        for key,value in d1.items():
            output.append((value, key))
        output.sort()
        result = []
        for value, key in output[-k:]:
            result.append(key)
        return result