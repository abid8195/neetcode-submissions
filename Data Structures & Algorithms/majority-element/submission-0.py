class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d1 = {}
        for n in nums:
            if n in d1:
                d1[n] += 1
            else:
                d1[n] = 1
        output = []
        for key,value in d1.items():
            output.append((value, key))
        output.sort()
        if output[len(output) -1][0] > len(nums) / 2:
            return output[len(output) -1][1] 
     
     
        
        