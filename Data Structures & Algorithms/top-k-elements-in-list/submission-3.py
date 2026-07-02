class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for n in nums:
            if n in d1:
                d1[n] += 1
            else:
                d1[n] = 1
        arr = []
        for num, cnt in d1.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
     
     
        