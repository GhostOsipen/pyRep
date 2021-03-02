# Given a string s consists of some words separated by spaces, 
# return the length of the last word in the string. 
# If the last word does not exist, return 0.

def lengthOfLastWord(s: str) -> int:
    count = 0
    rs = s[::-1]
    for i in rs:
        if i == " ":
            count += 1
        else:
            break
    
    if count != 0:
        rs = s[-(count + 1)::-1]

    count = 0   
    for i in rs:
        if i != " ":
            count += 1
        else:
            break
    
    return count
     
        

print(lengthOfLastWord("     "))
