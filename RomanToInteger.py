# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

def roman_to_int(s: str) -> int:
    answer = 0

    table = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

    for i in reversed(range(len(s))):
        answer += table[s[i]]
        if s[i+1] == 'V':
            print('qwerty')

        
    return answer


print(roman_to_int('IV'))