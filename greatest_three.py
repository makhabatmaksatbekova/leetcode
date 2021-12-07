# Given an array of integers, return the greatest three.
array = [2,3,4,5,6,8]
def find_greates_three(n):

    hash_table = {}
    for el in n:
        if el not in hash_table:
            hash_table[el] = el
        else:
            hash_table[el] = False


    for index in range(len(array)):
        if hash_table[array[index]] > array[index + 1]:
            
