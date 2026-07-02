class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        output = []
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, n in count.items():
            freq[n].append(i)
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                output.append(num)
                if len(output) == k:
                    return output
        
     
     
        