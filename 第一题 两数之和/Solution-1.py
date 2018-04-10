class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        result = []
        for index, num in enumerate(nums):
            numMap[num] = index
        
        for index, num in enumerate(nums):
            key = target - num
            firstNumIndex = numMap.get(key)
            if key in numMap and firstNumIndex != index:
                result.append(firstNumIndex)
                result.append(index)
                break
        return result

sol = Solution()

print(sol.twoSum([-1,-2,-3,-4,-5], -8))