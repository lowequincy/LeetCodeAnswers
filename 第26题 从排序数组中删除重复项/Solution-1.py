class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = None
        for index in range(len(nums)):
            if pre != nums[0]:
                pre = nums[0]
                nums.append(pre)
            nums.pop(0)

        return len(nums)

sol = Solution()
sol.removeDuplicates([0,0,0,0])