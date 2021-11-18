class Solution:
    def missingNumber(self, nums):
        for number in range(0, (max(nums) + 2)):
            if number not in nums:
                return number
            
result = Solution()
print(result.missingNumber([0,1]))