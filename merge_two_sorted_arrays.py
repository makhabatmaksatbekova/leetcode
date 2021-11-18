

n1 = [1, 2, 4, 5]
n2 = [6]
mm = len(n1)
nn = len(n2)

# def merge(nums1, m, nums2, n):
#     k = n + m - 1
#     i = m - 1
#     j = n - 1
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             k = k - 1
#             i = i - 1
#         else:
#             nums1[k] = nums2[j]
#             k = k - 1
#             j = j - 1
#     while j >= 0:
#         nums1[k] = nums2[j]
#         k = k - 1
#         j = j - 1


def merge(nums1, m, nums2, n):
    i,j = 0,0
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            i+=1
        elif nums2[j]<=nums1[i]:
            m+=1
            for k in range(m-1,i,-1):
                nums1[k] = nums1[k-1]
            nums1[i] = nums2[j]
            j+=1
            i+=1
        
        while j<n:
            nums1[i] = nums2[j]
            j+=1
            i+=1   
    print(n1)
print(merge(n1, mm, n2, nn))
print(n1)