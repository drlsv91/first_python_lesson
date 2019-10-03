# temperature = 15
# if temperature > 30:
#     print("it's warm")
#     print("Drink water")
# elif temperature > 20:
#     print("it's nice")
# else:
#     print("It's cold")
# print("Done")
# Tenary operator

# age = 12
# # if age >= 18:
# #     message = "Eligible"
# # else:
# #     message = "Not Eligible"
# # this is a Tenary Operator
# message = "Eligible" if age >= 18 else "Not Eligible"
# print(message)


# Logical Operator in python
# # and| or| and not|
# high_credit = False
# high_income = True
# student = True
# # if (high_credit or high_income) and not student:
# #     print("Eligible")
# # else:
# #     print("not Eligible")
# message = "Eligible" if high_income and high_credit else "Not Eligible"
# print(message)

# condition chaining
# age should be between 18 and 65
# age = 22
# if 18 <= age < 65:
#     print("eligible")
# else:
#     print("note eligible")
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("sucessful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(5):
#     for y in range(3):
#         print(f"[{x}, {y}]")

# print(type(range(5)))
# arr = [1, 2, 4, 5, 6]#this is a list
# for x in arr:
#     print(x)
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# while True:
#     command = input(">>>")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         print(number)
#         count += 1
# print(f"we have {count} even numbers")
