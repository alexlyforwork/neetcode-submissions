class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        last2_house = 0
        last1_house = nums[0]
        for i in range(1,n):
            curr = max(last1_house,last2_house+nums[i])
            last2_house = last1_house
            last1_house = curr
        return curr

