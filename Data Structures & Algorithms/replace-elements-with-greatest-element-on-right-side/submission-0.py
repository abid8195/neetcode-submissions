class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maxo = 0
            if i == len(arr)-1:
                arr[i] = -1
            else:
                for j in range(i + 1, len(arr)):
                    maxo = max(maxo,arr[j])
                arr[i] = maxo
        return arr
        
        