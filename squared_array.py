# Given two integer arrays,  
# return true if every value in the first array
#  has it's corresponding value squared in the second array.


nums1 = [2,3,4]
nums2 = [4,9,16]
def squared_array(n1, n2):
    
    hash_table = {}

    for n in n1:
        if n**2 not in hash_table:
            hash_table[n**2]=True
        else:
            hash_table[n**2]=False

    for n in n2:
        if n not in hash_table:
            return False 
    return True 


print(squared_array(nums1, nums2))