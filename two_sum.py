from typing import List

nums = [2,7,11,15]
target = 9
Output = [0,1]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for a_index in range(len(nums)-1):
            b_index = a_index + 1
            for b_index in range(a_index+1, len(nums)):
                if nums[a_index] + nums[b_index] == target:
                    return [a_index,b_index]


        
sol = Solution()
result = sol.twoSum(nums, target)
print(result)