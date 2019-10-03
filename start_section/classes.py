# CLASSES
# a class is a blueprint for creating new object
# an object is an instance of a class

# CREATING CUSTOME CLASS IN PYTHON


# class Point:
#     def draw(self):
#         print("draw")


# point = Point()

# print(point)

# class Point:
#     def __init__(self, x, y):  # this is the constructor function
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(1, 2)
# print(point.x)


# CLASSES VS INSTANCE ATTRIBUTE
# class attribute are shared by all instances of the class
# class Point:
#     default_color = "red"

#     def __init__(self, x, y):  # this is the constructor function
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(1, 2)
# another = Point(3, 4)
# point.z = 10

# print(another.default_color)
# print(point.default_color)


# class Solution:
#     def twoSum(self, nums, target):
#         storage = {}
#         for i, num in enumerate(nums):
#             n = target - num
#             print(n)
#             if n not in storage:
#                 storage[num] = i
#             else:
#                 return [storage[n], i]


# sum_num = Solution()
# print(sum_num.twoSum([2, 7, 11, 15], 9))

# CLASS VS INSTANCE METHODS
# class Point:

#     def __init__(self, x, y):  # this is the constructor function
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point.zero()
# print(point.draw())

# MAGIC METHODS
# they are the method that have two underscore before their names
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"{self.x}, {self.y}"

#     def draw(self):
#         print(f"Point({self.x}, {self.y})")


# point = Point(2, 3)
# # print(point.__str__())
# print(str(point))

# COMPARING OBJECTS
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(10, 20)
# other = Point(1, 2)
# # print(point == other)
# print(point > other)

# SUPPORTING ARITHMETIC OPERATION
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(10, 20)
# other = Point(1, 2)
# combined =point + other
# print(combined.x)


# CREATING CUSTOM CONTAINERS
# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud["python"])


# PRIVATE MEMBERS
# class TagCloud:
#     def __init__(self):
#         self.__tags = {} #__ is a convention that indicates that tags is private

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.__tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.__tags)

#     def __iter__(self):
#         return iter(self.__tags)


# cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud._TagCloud__tags)

# PROPERTIES
# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("price can not be negative")
#         self.__price = value

# product =Product(10)
# print(product.price)


# INHERITANCE
# class Animal:
#     def __init__(self):
#         self.age = 10
#     def eat(self):
#         print("eat")

# class Mammal(Animal):
#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m = Mammal()
# print(m.age)


# THE OBJECT CLASS
# all class inherit from the object class in python
# METHOD OVERRIDING
# replacing or extending a method define in the base  class

# class Animal:
#     def __init__(self):
#         print("Animal contructor")
#         self.age = 10
#     def eat(self):
#         print("eat")

# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("mammal constructor")
#         self.weight =20
#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m = Mammal()
# print(m.age, m.weight)

# MULTI-LEVEL INHERITANCE
# MULTIPLE INHERITANCE
# a good example of multiple inheritance is a fish that can swim and fly

# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):
#     pass


# f = FlyingFish()


# A GOOD EXAMPLE OF INHERITANCE
# from abc import ABC, abstractmethod
# class InvalidOperationError(Exception):
#     pass
# class Stream(ABC): #making this class abstract so we derive it from the abc class
#     def __init__(self):
#         self.opened=False
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("stream is already close")
#         self.opened = False
# # ABSTRACT BASE CLASSES
#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")

# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")

# class MemoryStream(Stream):
#     def read(self): #it must also contain the read method for it to be instantiated
#         pass
# # stream = Stream() #we cannot instantiate abstract class
# stream = MemoryStream()
# print(stream.open())

# # POLYMORPHISM
# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
# class TextBox(UIControl):
#     def draw(self):
#         print("textbox")

# class DropDownList(UIControl):
#     def draw(self):
#         print("dropdown list")

# def draw(controls):
#     for control in controls:
#         control.draw()


# ddl = DropDownList()
# textbox = TextBox()
# print(draw([ddl, textbox])) # this is called polymorphism the draw method does not know the control isworking with this is determined at runtime

# DUCK TYPING
# without the UIcontrol it still work thesame as long as it is interable and it have the draw function it will work and achieve polymorphic behaviour.
# class TextBox:
#     def draw(self):
#         print("textbox")

# class DropDownList:
#     def draw(self):
#         print("dropdown list")

# def draw(controls):
#     for control in controls:
#         control.draw()


# ddl = DropDownList()
# textbox = TextBox()
# print(draw([ddl, textbox]))

# EXTENDING BUILD-IN-TYPES
# class Text(str):
#     def duplicate(self):
#         return self + self
# text = Text("Python")
# print(text.duplicate().lower())

# class TrackableList(list):
#     def append(self, object):
#         print("Append called")
#         super().append(object)


# list = TrackableList()
# print(list.append("1"))

# DATA CLASSES
# from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p1 = Point(x=1, y=3)
# p2 = Point(x=1, y=3)

# print(p1 == p2)