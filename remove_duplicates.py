class Solution:
    def removeDuplicates(self, nums):
        lenth = 0
        duplicate = nums[1]
        for i in range(len(nums)-1):
            if duplicate == nums[i]:
                duplicate = nums[i]
                nums.remove(nums[i])
                lenth = len(nums)
                nums.append("-")
        return lenth

result = Solution()
print(result.removeDuplicates([1,1,2]))