class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s, prof, maxprof = 0, 0, 0
        for e in range(1, len(prices)):
            if prices[e] < prices[s]:
                s = e
            else:
                prof = prices[e] - prices[s]
                maxprof = max(maxprof, prof)
            e += 1
        return maxprof
        