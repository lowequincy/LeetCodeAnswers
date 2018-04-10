class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        for index in range(0, len(nums)):
            if nums[index] in numMap:
                return numMap[nums[index]], index
            numMap[target - nums[index]] = index
                
sol = Solution()
print(sol.twoSum([-1,-2,-3,-4,-5], -8))