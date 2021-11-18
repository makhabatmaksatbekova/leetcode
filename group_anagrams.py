
def groupAnagrams(strs):
    str_dic = {}
    anagram_list = []
    for string in strs:
        str_dic[string] = "".join(sorted(string))
    return str_dic
            
    # for string in strs:
    #     if str_dic.get(string):

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))