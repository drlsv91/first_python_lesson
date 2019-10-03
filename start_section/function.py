# # def greet():
# #     print("hello world")


# # greet()
# def evenNumbers(num):
#     count = 0
#     for number in range(1, num):
#         if number % 2 == 0:
#             count += 1
#             print(number)
#     return(f"we have {count} even numbers")


# # print(evenNumbers(100))
# # print(my_num)

# def increment(number, by):
#     return number + by


# # you can optionally include the arguments when passing the parameter to a function
# # print(increment(2, by=1))
# # default parameter
# def decrement(number, by=1):
#     return number - by


# # print(decrement(4, 3))

# # passing multiple arguments to a function
# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))
# # dictionary in python


# def save_user(**user):
#     return user["job"]
# # print(save_user(id=1, name = "victor", job = "fullstack", start=True))
