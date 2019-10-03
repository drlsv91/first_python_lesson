# EXCEPTIONS
# To use exception handling in Python, you first need to have a catch-all except clause. The words "try" and "except" are Python keywords and are used to catch exceptions. try-except [exception-name] (see above for examples) blocks The code within the try clause will be executed statement by statement
# an exception is a kind of error that terminate the wxcution of a program
# try:
#     age = int(input("Age:"))
# except ValueError as ex:
#     print("You didnt give a number")
#     print(ex)
# print("excution continues")


# HANDLING DIFFERENT EXCEPTIONS
# try:
#     age = int(input("Age:"))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You didnt enter a valid age")
# else:
#     print("No exceptions were thrown")


# CLEANING UP
# try:
#     file = open("exceptions.py")
#     age = int(input("Age:"))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You didnt enter a valid age")
# else:
#     print("No exceptions were thrown")
# finally:  # it is use to release external resources
#     file.close()

# THE WITH STATEMENT
# try:
#     with open("exceptions.py") as file:
#         print("file open")
#     age = int(input("Age:"))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print("You didnt enter a valid age")
# else:
#     print("No exceptions were thrown")


# RAISING EXCEPTIONS

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("age cannot be zero or less")
#     return 10/age


# try:
#     calculate_xfactor(-1)
# except ValueError as ex:
#     print(ex)

# COST OF RAISING EXCEPTIONS
# from timeit import timeit
# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#       return None
#     return 10/age


# xfactor = calculate_xfactor
# if xfactor == None:
#     pass
#     """


# print("first code", timeit(code1, number=1000))
