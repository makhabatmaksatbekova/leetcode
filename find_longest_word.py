# Find the length of the longest word in a sentence.
s = "I love challenging problems."
s = s.split(" ")



def longest_word(s):
    print(s)
    longest = s[0]
    for index in range(1, len(s)):
        if len(s[index]) > len(longest):
            longest = s[index]
    return longest
        

print(longest_word(s))
