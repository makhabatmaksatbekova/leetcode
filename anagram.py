# Write a function to check whether two given strings are anagram of each other or not. 
# An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
# For example, “abcd” and “dabc” are an anagram of each other.

s1 = "anagram"
s2 = "nagaram"

#There is also Counter method from collections 
#Ask interviewer if you can use sort method, if you can use sort build in method, then you can sort two strings and compare them:
# return sort(s1) == sort(s2)

def check_for_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False 
    dict_1 = {}
    dict_2 = {}

    for ch in s1:
        if ch in dict_1:
            dict_1[ch]+= 1
        else:
            dict_1[ch] = 1

    for ch in s2:
        if ch in dict_2:
            dict_2[ch]+= 1
        else:
            dict_2[ch] = 1

    if dict_1 != dict_2:
        return False 
    return True 

print(check_for_anagrams(s1,s2))

