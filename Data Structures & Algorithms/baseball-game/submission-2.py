class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        ops = []
        sum = 0
        for i in range(n):
            op = operations[i]
            if op == "+":
                ops.append(int(ops[-1]) + int(ops[-2]))
            elif op == "D":
                ops.append(int(ops[-1]) * 2)
            elif op == "C":
                ops.pop()
            else:
                ops.append(int(op))
        for i in range(len(ops)):
            sum += int(ops[i])
        return sum
