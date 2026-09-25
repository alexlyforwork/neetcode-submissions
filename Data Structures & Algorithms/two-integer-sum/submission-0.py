class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = dict()
        for i,num in enumerate(nums):
            if num in freq:
                return [freq[num],i]
            freq[target-num] = i
        