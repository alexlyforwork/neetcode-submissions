class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += 1 if (1<<i)&n else 0
        return res
