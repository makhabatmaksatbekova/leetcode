# Given two arrays, write a function to compute their intersection. 
# Example input: nums1 = [1,2,2,1], nums2 = [2,2]. Output: [2,2].
# if it is required to return only unique characters, create a set(), instead of a list. 

nums1 = [1,2,2,1]
nums2 = [2,2]

def find_intersection(n1,n2):
    dict1 = {}

    for el in n1:
        if el in dict1:
            dict1[el] = True
        else:
            dict1[el] = False 

    intersection = []
    for ch in n2:
        if ch in dict1:
            intersection.append(ch)

    return intersection

print(find_intersection(nums1,nums2))