#=======================
# x = int(input())
# h = 60 * int(input())
# m = int(input())
# print(((h+m) + x)//60)
# print(((h+m) + x)%60)
#=======================
# a = int(input())
# b = int(input())
# h = int(input())

# if a <= h <= b:
#     print("Это нормально")
# elif h < a:
#     print("Недосып")
# elif h > b:
#     print("Пересып")
#======================
# year = int(input())
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("Високосный")
#         else: 
#             print("Обычный")    
#     else:
#         print("Високосный")       
# else:
#     print("Обычный")
#======================
# import math
# a = int(input())
# b = int(input())  
# c = int(input())

# p = (a+b+c)/2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(s)
#======================
# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or a >= 19:
#     print(True)
# else:
#     print(False)
#======================
# a = float(input())
# b = float(input())  
# o = input()

# if o == "+":
#     print(a+b)
# elif o == "-":
#     print(a-b)
# elif o == "/":
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a/b)
# elif o == "*":
#     print(a*b)
# elif o == "mod":
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a%b)
# elif o == "pow":
#     print(a**b)
# elif o == "div":
#     if b == 0:
#         print("Деление на 0!")
#     else:
#         print(a//b)
#======================
# import math
# t = input()

# if t == "треугольник":
#     a = int(input())
#     b = int(input())  
#     c = int(input())
#     p = (a+b+c)/2
#     print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
# elif t == "прямоугольник":
#     a = int(input())
#     b = int(input())
#     print(a*b)
# elif t == "круг":
#     r = int(input())
#     print(3.14 * r ** 2)
#======================
# a = int(input())
# b = int(input())  
# c = int(input())

# nums = [a,b,c]
# print(max(nums))
# print(min(nums))
# nums.remove(max(nums))
# nums.remove(min(nums))
# other = nums[0]
# print(other)
#====================== 
# n = int(input())

# if (n % 10) == 1:
#     print(n, "программист") if (n % 100) != 11 else print(n, "программистов")
# elif (n % 10) == 2 or (n % 10) == 3 or (n % 10) == 4:
#     print(n, "программиста") if (n % 100) != 12 and (n % 100) != 13 and (n % 100) != 14 else print(n, "программистов")
# else:
#     print(n, "программистов")
#====================== 
# n = input()
# print("Счастливый") if int(n[0])+int(n[1])+int(n[2]) == int(n[3])+int(n[4])+int(n[5]) else print("Обычный")
#======================
# s = 0
# n = 1
# while n != 0:
#     n = int(input())
#     s += n
# print(s)
#======================
# a = int(input())
# b = int(input())
# d = 1
# while d % a != 0 or d % b != 0:
#     d += 1
# print(d)
#======================
# a = 0
# while a <= 100:  
#     a = int(input())
#     if a < 10:
#         continue
#     elif a > 100:
#         break
#     print(a)
#======================
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(end='\t')
# for i in range(c, d + 1):
#     print(i, end='\t')
# print()
# for i in range(a, b + 1):
#     print(i, end='\t')
#     for j in range(c, d + 1):
#         print(i*j , end='\t')
#     print()
#======================
# a = int(input())
# b = int(input())
# s = 0
# count = 0

# for i in range(a, b + 1):
#     if i % 3 == 0:
#         s += i
#         count += 1
# print(s / count) 
#======================
# a = input()

# g = a.count('g') + a.count('G')
# c = a.count('c') + a.count('C')

# print(((g + c)/len(a)) * 100)
#======================
# a = input()
# b = ""
# s = ""
# count = 0

# for i in range(len(a)):
#     if a[i] != b:
#         b = a[i]
#         for j in a[i:]:
#             if j == b:
#                 count += 1
#             else:
#                 break
#         s += b + str(count)    
#         count = 0
# print(s)
#======================
# a = [int(i) for i in input().split()]
# print(sum(a))
#======================
# a = [int(i) for i in input().split()]
# if len(a) == 1:
#     print(a[0])
# else:
#     for i in range(len(a)):
#         if i + 1 > len(a) - 1:
#             print(a[i-1] + a[0], end = " ")
#         else:
#             print(a[i-1] + a[i + 1], end = " ")
#======================
# a = [int(i) for i in input().split()]
# a.sort()
# b = float("inf")
# s = ""

# for i in range(len(a)):
#     if b != a[i]:
#         b = a[i]
#         if a.count(b) > 1:
#             s += str(b) + " " 
# print(s)
#======================