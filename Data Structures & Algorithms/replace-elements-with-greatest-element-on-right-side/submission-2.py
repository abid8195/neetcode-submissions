class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        for i in range(n):
            maxo = -1
            for j in range(i + 1, len(arr)):
                maxo = max(maxo,arr[j])
            ans[i] = maxo
        return ans
        
        