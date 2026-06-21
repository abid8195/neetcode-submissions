class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x, y = 0, 0
        output = 0
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()

            if x == y:
                continue
            if x < y:
                y = y - x
                stones.append(y)
        if len(stones) == 0:
            return output
        else:
            output = stones[-1]
            return output
        