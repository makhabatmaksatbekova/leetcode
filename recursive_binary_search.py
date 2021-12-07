def recursive_binary_search(array, to_find, low=0, high=None):
    if high is None:
        high = len(array)

    if low >= high:
        return None

    mid = (high + low) // 2

    if array[mid] == to_find:
        return mid
    elif array[mid] > to_find:
        high = mid
    else:
        low = mid + 1

    return recursive_binary_search(array, to_find, low, high)

print(recursive_binary_search([1,2,3,4,5,6,7,8],9))