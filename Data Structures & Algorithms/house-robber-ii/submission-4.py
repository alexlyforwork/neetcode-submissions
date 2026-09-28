class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob_linear(houses):
            last2_house = 0
            last1_house = 0
            for house in houses:
                last2_house, last1_house = last1_house, max(last1_house,last2_house+house)
            return last1_house
        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))