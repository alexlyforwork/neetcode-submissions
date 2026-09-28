class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        last2_house = 0
        last1_house = 0
        for num in nums:
            last2_house, last1_house = last1_house, max(last1_house,last2_house+num)
        return last1_house

