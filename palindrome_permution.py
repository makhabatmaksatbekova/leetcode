# # Write an efficient function that checks whether any permutation of an input string is a palindrome. 
# A String is called Palindrome if it reads the same backwards as well as forwards. For example, the String  can be read the same backwards as well as forwards.
# Now, a Permutation of a String S is some String K where S and K contain the same set of characters, however, these characters need not necessarily have the same positions. For Example, consider the String . Here, the Strings :

# are all permutations of it.

# Now, given a String S consisting of lowercase English alphabets, you need to find out whether any permutation of this given String is a Palindrome. If yes, print "YES" (Without quotes) else, print "NO" without quotes.


def palindrom_permutation(s):
    char_dict = {}
    for ch in s:
        if ch in char_dict:
            char_dict[ch] +=1
        else:
            char_dict[ch] = 1

    odd_count = 0
    for value in char_dict.values():
        if value % 2:
            odd_count += 1
           
    if odd_count > 1:
        return False 
    return True 

print(palindrom_permutation("ababct"))
        
            



    
