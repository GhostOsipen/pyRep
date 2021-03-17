# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
import math

def reverse(x: int) ->int:
    nums: list = []
    s = ""
    for i in str(abs(x)):
        nums.append(int(i))
    for i in nums[::-1]:
        s = s + str(i)
    if x >= 0 and int(s) <= 2147483647:
        return int(s)
    elif x < 0 and -int(s) >= -2147483647:
        return -int(s)
    else:
        return 0

def reverse2(x: int) -> int:
    if x >= 0 and int(str(x)[::-1]) <= 2147483647:
        return int(str(x)[::-1])
    elif x < 0 and -int(str(abs(x))[::-1]) >= -2147483647:
        return -int(str(abs(x))[::-1])
    else:
        return 0
    


print(reverse(-123))