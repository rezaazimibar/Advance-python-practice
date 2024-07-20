# ---------------------------------------iterable-------------------------------

# iterable is any object that we can loop through

# range() is an iterable and also is a generator
# list() is an iterable but not a generator
# in fact anything that are generators it is also an iterable
# but anything that are an iterable not always not a generator

# def generator_func(num):
#     for i in range(num):
#         yield i
#
#
# g = generator_func(100)
# next(g)
# next(g)
# next(g)
# print(next(g))
# for item in generator_func(100):
#     print(item)


# def my_generator_func(num):
#     for i in range(num):
#         yield i
#
#
# generator = my_generator_func(10)
# print(next(generator))
# print(next(generator))

# def my_generator(num):
#     for i in range(num):
#         yield i ** 2
#
#
# generator1 = my_generator(100)
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")
# print(f"my generator is: {next(generator1)}")

# ----------------------------generators-performance----------------------------
# from time import time
#
#
# def performance(func):
#     def warp_func(*args, **kwargs):
#         time1 = time()
#         func(*args, **kwargs)
#         time2 = time()
#         print(f"the time is: {time2 - time1}")
#
#     return warp_func
#
#
# @performance  # generators are faster than regular iterable
# def my_generator(num):
#     print("1)")
#     for i in range(num):
#         i * 5
#
#
# @performance
# def my_iterable(num):
#     print("2)")
#     for i in list(range(num)):
#         i * 5
#
#
# my_generator(100000000)
# my_iterable(100000000)

# -----------------------------------build-own-generators-iterable------------------------------

# def special_loop(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
#
#
# special_loop([1, 2, 3, 74, 5, 6])
#
#
# class MyGen:
#
#     def __init__(self, first, last):
#         self.current = first
#         self.first = first
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current < self.last:
#             num = self.current
#             self.current += 1
#             return num
#         raise StopIteration
#
#
# gen = MyGen(30, 110)
# for i in gen:
#     print(i)

# ----------------------------------exersice---------------------------------

# def my_fib(num):
#     first = 1
#     item = 1
#     if num==1:
#         print(1)
#     else:
#         for i in range(2, num):
#             item = first - item
#             first = first + item
#
#             print(f"empty: {i}")
#             print(first)
#
#
# my_fib(10)

# def my_fib2(num):
#     a = 0
#     b = 1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = b + temp
#
#
# for i in my_fib2(10):
#     print(i)
