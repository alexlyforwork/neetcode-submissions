class Solution:
    def rob(self, nums: List[int]) -> int:
        [2,1,1,2]
        [2,2,3,]

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        last1_house = max(nums[1],nums[0])
        last2_house = nums[0]
        for i in range(2,n):
            curr = max(last1_house,last2_house+nums[i])
            last2_house = last1_house
            last1_house = curr
        return curr

