#Високосный год (2)
# Написать функцию is_year_leap, принимающую 1 аргумент — год, 
# и возвращающую True, если год високосный, и False иначе.

def is_year_leap(year: int) -> bool:
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else: return False    
        else: return True        
    else: return False        
            
print(is_year_leap(2016))
