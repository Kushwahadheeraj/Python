# # for i in range(5):
# #     print("Iteration:", i)
    
# # # while loop
# # count = 0   
# # while count < 5:
# #     print("Count:", count)
# #     count += 1

# # # break statement
# # for i in range(10):
# #     if i == 5:
# #         break
# #     print("Iteration:", i)
    
# # # continue statement
# # for i in range(10):
# #     if i == 5:
# #         continue
# #     print("Iteration:", i)

# # pass statement
# # for i in range(10):
# #     if i == 5:
# #         pass
# #     print("Iteration:", i)

# - Accept an integer and Print hello world n times 


# n = int(input("Enter a number: "))
# for i in range(n):
#     print("Hello, World!")

# - Print natural number up to n 

# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print(i)

# - Reverse for loop. Print n to 1 

# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     print(i)

# - Print the sum of all numbers in a list 
# list1 = [1, 2, 3, 4, 5]
# sum = 0
# for i in list1:
#     sum += i
# print("Sum:", sum)

# - Print the product of all numbers in a list 
# list1 = [1, 2, 3, 4, 5]
# product = 1
# for i in list1:
#     product *= i
# print("Product:", product)

# - Print the sum of all even numbers in a list 
# list1 = [1, 2, 3, 4, 5]
# sum = 0
# for i in list1:
#     if i % 2 == 0:
#         sum += i
# print("Sum of even numbers:", sum)

# - Print the sum of all odd numbers in a list 
# list1 = [1, 2, 3, 4, 5]
# sum = 0
# for i in list1:
#     if i % 2 != 0:
#         sum += i
# print("Sum of odd numbers:", sum)

# separately 
# n = int(input("Enter a number: "))
# sum_even = 0
# sum_odd = 0
# for i in range(1, n + 1): 
#     if i % 2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)


# - Print all the factors of a number 
# n = int(input("Enter a number: "))
# print("Factors of", n, "are:")
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)      


# - Accept a number and check if it a perfect number or not.

#  A number whose sum of factors is equal to the number itself 


#  Ex - 6 = 1, 2, 3 = 6


# n = int(input("Enter a number: "))
# sum_of_factors = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum_of_factors += i
# if sum_of_factors == n:
#     print(f"{n} is a perfect number.")
# else:    print(f"{n} is not a perfect number.") 



# Check wether the number is prime or not

# n = int(input("Enter a number: "))
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{n} is a prime number.")
# else: 
#     print(f"{n} is not a prime number.")


#     - Count all letters, digits, and special symbols from a given 
# string

#  Given: str1 = "P@#yn26at^&i5ve"

#  Expected Outcome:

#  Total counts of chars, digits, and symbols

#  Chars = 8

#  Digits = 3

#  Symbol = 4




# str1 = "P@#yn26at^&i5ve"
# chars = 0
# digits = 0
# symbols = 0
# for char in str1:
#     if char.isalpha():
#         chars += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         symbols += 1
# print("Chars =", chars)
# print("Digits =", digits)
# print("Symbols =", symbols)

# Reverse a string without using in build functions.4

# str1 = "P@#yn26at^&i5ve"
# reversed_str = ""
# for char in str1:
#     reversed_str = char + reversed_str
# print(reversed_str)

# Check string is Pallindrome or not
str1 = "madam"
reversed_str = ""
for char in str1: 
    reversed_str = char + reversed_str    
if str1 == reversed_str:    
    print("String is Pallindrome")    
else:    
    print("String is not Pallindrome")    
