# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false

# if condition:
#     # code to execute if condition is true
# elif another_condition:
#     # code to execute if another_condition is true
# else:
#     # code to execute if both conditions are false  

# if condition:
#     # code to execute if condition is true
#     if nested_condition:
#         # code to execute if nested_condition is true
#     else:
#         # code to execute if nested_condition is false  
# else:
#     # code to execute if condition is false 

# if condition:
#     # code to execute if condition is true
#     if nested_condition:
#         # code to execute if nested_condition is true
#     elif another_nested_condition:
#         # code to execute if another_nested_condition is true
#     else:
#         # code to execute if both nested conditions are false  
# else:
#     # code to execute if condition is false

# # if condition:
#     # code to execute if condition is true
# # elif another_condition:
#     # code to execute if another_condition is true
# # else: 
#     # code to execute if both conditions are false  


# a=10
# b=5

# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")


# if a>b:
#     print("a is greater than b")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("b is greater than a")

#     If- elif ladder
# @ You cna also create if elif ladder using multiple conditions of 
# elif.j
# @ For understanding solve this questionj
# @ take the input of temperature in celsiusX
# @ Below 0°C → "Freezing Cold b
# @ 0°C to 10°C → "Very Cold b
# @ 10°C to 20°C → "Cold b
# @ 20°C to 30°C → "Pleasant b
# @ 30°C to 40°C → "Hot b
# @ Above 40°C → "Very Hot "

temp=int(input("Enter the temperature in celsius: "))

if temp<0:
    print("Freezing Cold")
elif temp>=0 and temp<=10:
    print("Very Cold")
elif temp>10 and temp<=20:
    print("Cold")
elif temp>20 and temp<=30:
    print("Pleasant")
elif temp>30 and temp<=40:
    print("Hot")
else:
    print("Very Hot")       