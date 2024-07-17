# -----------------------------------Higher-order-function-(HOC)------------------------------------

# def say_something(func):  # a function that accept another function as an argument have height order function
#     func()
#     # map() is a higher order function because accept a function as argument
#
#
# def say_hello():
#     print("hello")
#
#
# say_something(say_hello)
#
#
# def return_something():  # a function that return another function also is a height order function
#     def some_value():
#         return 44
#
#     return some_value()
#
#
# print(return_something())

# -----------------------------------------------------Decorator-----------------------------------------

# def my_decorator(func):
#     def warp_func():
#         print("🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽")
#         func()
#         print("🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼")
#
#     return warp_func
#
#
# @my_decorator  # this just cant accept just one function that define under the this decorator
# def say_hello():
#     print("say hello")
#
#
# # a = my_decorator(say_hello) #what happened under need the hod
# # a()
# # or
# # my_decorator(say_hello)()  #these ar same
#
# @my_decorator
# def say_goodbye():
#     print("goodbye")
#
#
# def say_nothing():
#     print("ha ha i said something")
#
#
# say_hello()
# say_goodbye()
# say_nothing()

# def design_decorator(func):
#     def warp_func(*args, **kwargs):
#         print("ヾ(≧▽≦*)o[ ]~(￣▽￣)~*")
#         func(*args, **kwargs)
#         print("(★‿★) ✍(◔◡◔)✍(◔◡◔)")
#
#     return warp_func
#
#
# @design_decorator
# def say_somthing(something="gg"):
#     print(something)
#
#
# say_somthing("hey hey")  # to solve this problem we can use *args **keyword
#
# from time import time
#
#
# def performance(func):
#     def warp_func(*args, **kwargs):
#         time1 = time()
#         func(*args, **kwargs)
#         time2 = time()
#         print(f"the function time is {time2 - time1}")
#
#     return warp_func
#
#
# @performance
# def looping_func(num):
#     for char in num:
#         char ** 2
#
#
# num1 = range(1, 100000000)
# looping_func(num1)
