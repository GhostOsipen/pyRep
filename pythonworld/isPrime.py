# Простые числа (6)
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(a: int) -> bool:
    if a >= 0 and a <= 1000:
        for i in range(2,a):
            if (a % (i)) == 0:
                return True
        else:
                return False

for i in range(2,101):
    print(str(i) + " is " + str(is_prime(i)))