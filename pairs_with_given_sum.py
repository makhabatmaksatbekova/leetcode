# Imagine working on software that processes lists of numbers. 
# Create a function named pairs_with_given_sums 
# It finds the number of pairs of numbers in a 
# list which add up to a given sum. This function should take 
# in a list of whole numbers and a given sum as a parameters. 
# This function should have a return value of the integer of
#  number of pairs.

def find_pairs(sum, nums):
    hash_map = {}
    for num in nums:
        if hash_map.get(num):
            hash_map[num]+=1
        else:
            hash_map[num]=1
    counter = 0
    for index in range(len(nums)):
        difference = sum - nums[index] 
        if difference in hash_map:
            counter +=1
            hash_map.pop(difference)
            hash_map.pop(nums[index])
    return counter 

print(find_pairs(10,[-1,1,9,11,1]))
    
