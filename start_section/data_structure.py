# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters  # combining list
# print(len(chars))

# operation in list
# chars = list("Hello world")
# indx = chars.index(" ")
# # print(indx)
# # print(chars)
# hello = chars[0:indx]
# world = chars[indx+1:]
# hello_world = hello + world
# chars[indx] = "_"
# # print(chars)
# # skipping every second item
# numbers = list(range(20))  # range are iterable
# even = numbers[::2]
# reverse = numbers[::-1]
# print(reverse)

# unpacking a list
# numbers = [1, 2, 3, 4]
# # first, second, third, fourth = numbers
# first, second, *others = numbers
# print(first, second, others)


# looping list
# for index, letter in enumerate(letters):
#     print(index, letter)
# Adding to list
# letters.append("d")
# # add at specific index
# letters.insert(0, "_")
# letters.pop(0)  # removing item by index
# letters.remove("b")  # removing item by value
# del letters[0:3]  # removing a range of items
# letters = ["a", "b", "c", "r", "x", "y"]
# # find a item return it index if present or error to prevent the error part check if item is in list
# if "r" in letters:
#     idx = letters.index("r")
#     print(idx)
#     print(letters.count("r"))

# sorting list

# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# def sort_item(item):
#     return item[1]


# items.sort(key=lambda item:  item[1])
# mapping a list
# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)
# print(sort_item(items))
# MAP FUNCTION

# items = [
#     ("product1", 10),
#     ("product2", 20),
#     ("product3", 12),
# ]
# # price = list(map(lambda item: item[1], items))
# # COMPREHENSION ==============================
# # this does thesame thing as the map function
# prices = [item[1] for item in items]
# # filtered = list(filter(lambda item: item[1] > 10, items))
# # this does thesame thing as the filter function
# filtered = [item for item in items if item[1] > 10]
# print(filtered)


# ZIP FUNCTION
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# # [(1,10), (2,20), (3,30)]
# x = list(zip("abc", list1, list2))
# print(x)


# STACKS LIFO
# implemented in the browser during Navigation from one web address to the other
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# # redirect to the last item in the list
# print("redirect", browsing_session[-1])
# # if no item in the list diable the back button
# browsing_session.pop()
# print("redirect", browsing_session[-1])
# browsing_session.pop()
# if not browsing_session:
#     print("disable button")

# QUEUES FIFO
# for efficiency sake will import the queue module from collection
# from collections import deque

# queue = deque([])
# print(queue)
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# first = queue.popleft()
# print(first)
# queue.popleft()
# print(queue)
# queue.popleft()

# if not queue:
#     print("Empty")

# TUPLES
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets

# convert list to tuple
# point = tuple([1, 2])*4
# point = tuple([1, 2])
# point = (1, 2, 3)
# print(point[0])


# SWAPPING VARIABLES
# x = 10
# y = 11
# # z = x
# # x = y
# # y = z
# x, y = y, x
# print(x, y)

# ARRAYS
# # u can use array if you are expriencing performance issue else use list and tuples by default
# from array import array
# numbers = array("i", [1, 2, 3])
# numbers.append(4)
# print(numbers)


# # SETS
# A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python's set class represents the mathematical notion of a set
# they are unordered so they cannot be accessed using  an index
# numbers = [1,1,3,4,4,5]
# first = set(numbers)
# second ={1,4,8}
# union = first | second
# intersection = first & second
# difference = first - second
# symmetric_diff = first ^ second
# print(union)
# print(intersection)
# print(symmetric_diff)

# DICTIONATIES
# Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. ... Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a 'comma'.
# point = {"x":1, "y":2} #declaring dictionary explicitly
# point = dict(x=1, y=2)  # using inbuilt function such as set(), list(), tuple()
# # accessing value by index
# point["x"]
# point["z"] = 20
# # del point["y"]
# print(point)
# if "a" in point:
#     print(point["a"])
# print(point.get("a", False))
# iterate over dictionary
# for key, value in point.items():
#     print(key, value)


# DICTIONARY COMPREHENSIONS
# values ={}
# for value in range(5):
#     values[value] = value*2
# dic_val = {value: value*2 for value in range(5)}#dictionary
# lis_val = [value*2 for value in range(5)]#list
# tuple_val = tuple((value*2 for value in range(5)))#tuple
# print(tuple_val)

# GENERATORS
# from sys import getsizeof
# # a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# # for val in values:
# #     print(val)
# values = (value*2 for value in range(1000000))  # generator object
# print("gen: ", getsizeof(values))


# UNPACKING OPERATOR
# This PEP proposes extended usages of the * iterable unpacking operator and ** dictionary unpacking operators to allow unpacking in more positions, an arbitrary number of times, and in additional circumstances
# it is thesame as the spread operator in JavaScript

# numbers = [1,2,3]
# unpack_num = *numbers #unpacking operator *
# values = list(range(10))
# values = [*range(10), *"hello"]#list
# first ={"x":1}
# second ={"x":10, "y":20}
# combined = {**first, "z":4, **second, "a":7}
# print(combined)
