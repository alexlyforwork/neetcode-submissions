class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        res = float('inf')
        for num in nums:   
            res = min(res,num)
        return res