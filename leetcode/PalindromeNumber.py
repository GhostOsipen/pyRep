# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.

def isPalindrome(x: int) -> bool:
    if x >= 0:
        nums = []
        s = ""
        for i in str(x):
            nums.append(int(i))
        for i in nums[::-1]:
            s = s + str(i)
        if int(s) == x:
            return True
        else:
            return False
    return False

def isPalindrome2(x: int) -> bool:
    return str(x) == str(x)[::-1] if x >= 0 else False
    # if x >= 0:
    #     return str(x) == str(x)[::-1]
    # else:
    #     return False 

print(isPalindrome2(121))