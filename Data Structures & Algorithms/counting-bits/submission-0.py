class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n+1):
            cnt = 0
            for i in range(32):
                if (1<<i)&num:
                    cnt +=1
            res.append(cnt)
        return res