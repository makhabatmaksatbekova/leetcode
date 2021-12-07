
# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
# def remove_dup(nums):
#     left = 0
#     right = left + 1
#     last = len(nums) -1
            
#     while nums[right] != -1:
#         if nums[left] == nums[right]:
#             nums.pop(nums[right])
#             nums.append(-1)
#         else:
#             left += 1
#     return nums 

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pointer = 0
        
        for index in range(1, len(nums)):
            if nums[pointer] != nums[index]:
                nums[pointer+1] = nums[index]
                pointer += 1
        return pointer + 1
                

print(removeDuplicates(nums))