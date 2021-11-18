string = "James"
string = list(string)

def reverse_str(s, r=""):
    r+=s[-1]
    s=s[:-1]
    if len(s) == 0:
        return(f"reversed string is {r}")
    else:
        reverse_str(s, r)

reverse_str(string)



def recursiveReverse(str, i = 0):
    n = len(str)
 
    if i == n // 2:
        return
     
    str[i], str[n-i-1] = str[n-i-1], str[i]
    recursiveReverse(str, i+1)
    return "".join(str)



print(recursiveReverse(string))

#  if using recursive function is not required, use while loop and rwo pointers 
def reverse_str(s):
    last = len(s)-1
    first = 0
  
    while first < last:
        s[first], s[last] = s[last], s[first]
        first += 1
        last -= 1
  
    return s