class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n ==2:
            return max(nums[0],nums[1])
        # rob first house
        last2_house = 0
        last1_house = nums[0]
        first=0
        for i in range(1,n-1):
            first = max(last1_house,last2_house+nums[i])
            last2_house = last1_house
            last1_house = first
        # rob last house
        last2_house = 0
        last1_house = nums[1]
        second=0
        for i in range(2,n):
            second = max(last1_house,last2_house+nums[i])
            last2_house = last1_house
            last1_house = second
        return max(first,second)