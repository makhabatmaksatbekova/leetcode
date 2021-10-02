# return number of differences between two strings 

str1= "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"

# def hamming_distance(str1, str2):
#     count = 0
#     for index in range(len(str1)):
#         if str1[index] != str2[index]:
#             count += 1
#     return count 


# Python zip() method takes iterable or containers 
# and returns a single iterator object,
# having mapped values from all the containers. 
# It is used to map the similar index of multiple 
# containers so that they can be used just using a single entity. 

def hamming_distance(str1, str2):
    return sum(letter1 != letter2 for letter1, letter2 in zip(str1, str2))


result = hamming_distance(str1, str2)
print(result)