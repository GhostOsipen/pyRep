# Given a non-empty array of decimal digits representing a non-negative integer,
# increment one to the integer.The digits are stored such that 
# the most significant digit is at the head of the list, and each element
# in the array contains a single digit.
# You may assume the integer does not contain any leading zero, 
# except the number 0 itself.

def plusOne(digits: list) -> list:
    temp = digits[::-1]
    count = 0

    for i in temp:
        if i == 9:
            count += 1
        else:
            break

    if count != len(temp):
        temp[0] += 1
        for i in range(len(temp)):
            if temp[i] > 9:
                temp[i] = 0
                temp[i + 1] += 1
    else:
        for i in range(len(temp)):
            temp[i] = 0
        temp.append(1)

    return temp[::-1]

def plus_one(digits: list) -> list:
    carry = False

    for i in reversed(range(len(digits))):
        digits[i] += 1
        if digits[i] > 9:
            digits[i] = 0
            carry = True
        else:
            carry = False
            break
    
    if carry:
        digits.insert(0, 1)
    
    return digits

print(plus_one([1,1,5,9]))
print(plus_one([1,1,1,9]))
print(plus_one([1,9,9,9]))
print(plus_one([9,9,9,9]))

