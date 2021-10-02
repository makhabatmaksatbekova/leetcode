# return number of differences between two strings 

str1= "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"

def hammer_diff(str1, str2):
    count = 0
    for index in range(len(str1)):
        if str1[index] != str2[index]:
            count += 1
    return count 

result = hammer_diff(str1, str2)
print(result)